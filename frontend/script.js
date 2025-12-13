// ==================== CONFIG ====================
const API_URL = 'http://localhost:5000';
const STORAGE_KEY = 'prediction_history';
const MAX_HISTORY = 20;

// ==================== STATE ====================
let predictionHistory = [];
let chart = null;
let darkMode = localStorage.getItem('darkMode') === 'true';

// ==================== INITIALIZATION ====================
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

function initializeApp() {
    loadHistory();
    setupEventListeners();
    checkAPIStatus();
    setDarkMode(darkMode);
    setInterval(checkAPIStatus, 10000);
}

// ==================== EVENT LISTENERS ====================
function setupEventListeners() {
    // Form submission
    document.getElementById('predictionForm').addEventListener('submit', handleSinglePrediction);



    // Dark mode toggle
    document.getElementById('darkModeToggle')?.addEventListener('click', toggleDarkMode);



    // Clear history
    document.getElementById('clearHistoryBtn')?.addEventListener('click', clearHistory);

    // Modal close
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    });
}

// ==================== SINGLE PREDICTION ====================
async function handleSinglePrediction(e) {
    e.preventDefault();

    const loading = document.getElementById('loading');
    const result = document.getElementById('result');

    result.classList.remove('success', 'error', 'warning');
    result.style.display = 'none';
    loading.style.display = 'block';

    const now = new Date();
    const data = {
        Product_Category: document.getElementById('category').value,
        Price: parseFloat(document.getElementById('price').value),
        Discount: parseFloat(document.getElementById('discount').value),
        Customer_Segment: document.getElementById('segment').value,
        Marketing_Spend: parseFloat(document.getElementById('marketing').value),
        Day: now.getDate(),
        Month: now.getMonth() + 1
    };

    // Validation
    if (data.Discount < 0 || data.Discount > 100) {
        loading.style.display = 'none';
        result.classList.add('error');
        result.innerHTML = `
            <h3 class="result-title"><i class="ph ph-warning"></i> Invalid Input</h3>
            <div class="prediction-value" style="font-size: 1.2rem;">Discount must be between 0% and 100%</div>
        `;
        result.style.display = 'block';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();
        loading.style.display = 'none';

        if (response.ok) {
            const prediction = responseData.predicted_revenue;

            result.classList.remove('error');
            result.classList.add('success');

            result.innerHTML = `
                <h3 class="result-title" id="resultTitle"><i class="ph ph-check-circle"></i> Prediction Successful</h3>
                <div class="prediction-value" id="predictionValue">$${responseData.predicted_revenue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div class="result-label" id="unitLabel">Projected Revenue</div>
            `;

            // Add to history
            addToHistory(data, responseData.predicted_revenue);

            // Show detailed results (Basic info only)
            showDetailedResults(data);
        } else {
            result.classList.remove('success');
            result.classList.add('error');
            result.innerHTML = `
                <h3 class="result-title" id="resultTitle"><i class="ph ph-warning-circle"></i> Error</h3>
                <div class="prediction-value" id="predictionValue">${responseData.error || 'Unknown Error'}</div>
            `;
        }

        result.style.display = 'block';
    } catch (error) {
        loading.style.display = 'none';
        result.classList.remove('success');
        result.classList.add('error');
        result.innerHTML = `
             <h3 class="result-title" id="resultTitle"><i class="ph ph-wifi-slash"></i> Connection Error</h3>
             <div class="prediction-value" id="predictionValue">Check if API is running</div>
        `;
        result.style.display = 'block';
    }
}

// ==================== BATCH PREDICTION ====================


// ==================== DISPLAY RESULTS ====================
function showDetailedResults(data) {
    let detailsHtml = `
        <div class="chart-container">
            <h4 class="chart-title"><i class="ph ph-chart-bar"></i> Input Summary</h4>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">Price</div>
                    <div class="stat-value">$${data.Price.toFixed(2)}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Discount</div>
                    <div class="stat-value">${data.Discount}%</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Budget</div>
                    <div class="stat-value">$${(data.Marketing_Spend).toLocaleString()}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Date</div>
                    <div class="stat-value" style="font-size:14px">${data.Day}/${data.Month}</div>
                </div>
            </div>
        </div>
    `;

    document.getElementById('result').innerHTML += detailsHtml;
}


// ==================== HISTORY ====================
function addToHistory(data, prediction) {
    const historyItem = {
        id: Date.now(),
        timestamp: new Date().toLocaleString('en-US'),
        category: data.Product_Category,
        price: data.Price,
        prediction: prediction
    };

    predictionHistory.unshift(historyItem);
    if (predictionHistory.length > MAX_HISTORY) {
        predictionHistory.pop();
    }

    saveHistory();
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const historyList = document.getElementById('historyList');
    if (!historyList) return;

    if (predictionHistory.length === 0) {
        historyList.innerHTML = '<p style="text-align: center; color: var(--text-muted);">No previous predictions</p>';
        return;
    }

    historyList.innerHTML = predictionHistory.map(item => `
        <div class="history-item">
            <div class="history-icon">
                <i class="ph ph-chart-line-up"></i>
            </div>
            <div class="history-details">
                <div class="history-category">${getCategoryName(item.category)}</div>
                <div class="history-time">${item.timestamp}</div>
            </div>
            <div class="history-result">$${item.prediction.toFixed(2)}</div>
        </div>
    `).join('');
}

function saveHistory() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(predictionHistory));
}

function loadHistory() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
        predictionHistory = JSON.parse(stored);
        updateHistoryDisplay();
    }
}

function clearHistory() {
    if (confirm('Are you sure you want to clear history?')) {
        predictionHistory = [];
        localStorage.removeItem(STORAGE_KEY);
        updateHistoryDisplay();
    }
}

// ==================== TABS ====================


// ==================== API STATUS ====================
async function checkAPIStatus() {
    const statusEl = document.getElementById('apiStatus');
    try {
        const response = await fetch(`${API_URL}/status`, { method: 'GET' });
        if (response.ok) {
            statusEl.innerHTML = '<i class="ph ph-check-circle"></i> API Connected';
            statusEl.className = 'status-badge connected';
        } else {
            statusEl.innerHTML = '<i class="ph ph-warning-circle"></i> API Down';
            statusEl.className = 'status-badge disconnected';
        }
    } catch {
        statusEl.innerHTML = '<i class="ph ph-wifi-slash"></i> API Offline';
        statusEl.className = 'status-badge disconnected';
    }
}

// ==================== DARK MODE ====================
function toggleDarkMode() {
    darkMode = !darkMode;
    setDarkMode(darkMode);
    localStorage.setItem('darkMode', darkMode);
}

function setDarkMode(enabled) {
    if (enabled) {
        document.body.classList.add('dark-mode');
        document.querySelectorAll('.container').forEach(el => el.classList.add('dark-mode'));
        document.querySelectorAll('header').forEach(el => el.classList.add('dark-mode'));
    } else {
        document.body.classList.remove('dark-mode');
        document.querySelectorAll('.container').forEach(el => el.classList.remove('dark-mode'));
        document.querySelectorAll('header').forEach(el => el.classList.remove('dark-mode'));
    }
}

// ==================== UTILITIES ====================
function getCategoryName(category) {
    const names = {
        'Electronics': 'Electronics',
        'Fashion': 'Fashion',
        'Home Decor': 'Home Decor',
        'Sports': 'Sports',
        'Toys': 'Toys'
    };
    return names[category] || category;
}

// ==================== EXPORT ====================
function exportHistory() {
    const csv = [
        ['Date', 'Product', 'Price', 'Prediction'].join(','),
        ...predictionHistory.map(item =>
            [item.timestamp, item.category, item.price, item.prediction].join(',')
        )
    ].join('\n');

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `predictions_${new Date().toLocaleDateString('en-US')}.csv`;
    link.click();
}

// ==================== FORM VALIDATION ====================
function validateForm() {
    const price = parseFloat(document.getElementById('price').value);
    const discount = parseFloat(document.getElementById('discount').value);
    const marketing = parseFloat(document.getElementById('marketing').value);

    if (price < 0 || discount < 0 || discount > 100 || marketing < 0) {
        alert('Please check input values');
        return false;
    }
    return true;
}

// ==================== KEYBOARD SHORTCUTS ====================
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        document.getElementById('predictionForm')?.dispatchEvent(new Event('submit'));
    }
});

// ==================== NOTIFICATIONS ====================
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    // Styles are now handled by CSS .notification classes
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
}
