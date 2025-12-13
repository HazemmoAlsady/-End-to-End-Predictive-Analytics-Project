# 📊 E-Commerce Sales Prediction - Advanced ML Forecasting System

A complete **end-to-end predictive analytics project** with REST API and professional web frontend for predicting e-commerce revenue using machine learning.

---

## ✨ Latest Code Updates (v2.0)

### Backend Changes
- **API Refactored:** Simplified endpoints structure (/, /status, /predict)
- **Feature Engineering:** Optimized feature order matching training data exactly
- **Error Handling:** Comprehensive validation for discount range (0-100%)
- **Special Cases:** 100% discount correctly returns $0.00 revenue
- **CORS Enabled:** Cross-origin requests supported for frontend integration
- **Model Loading:** Relative path resolution for portability

### Frontend Changes
- **HTML5 Structure:** 157 lines, semantic markup with Phosphor icons
- **CSS3 Redesign:** 755 lines with 50+ variables, full dark mode support
- **JavaScript Features:** 322 lines of vanilla JS with no external dependencies
- **Responsive Design:** Grid layout adapts from 1.2fr/0.8fr to 1fr at 900px
- **Dark Mode:** Complete theme system with localStorage persistence
- **History System:** 20-item limit, automatic localStorage sync
- **API Status:** Real-time connection monitoring with 10-second intervals
- **CSV Export:** Download predictions with date-stamped filenames
- **Form Validation:** Client-side checks before submission
- **Animations:** Smooth transitions (slideUp, slideIn, spin)

### Design Improvements
- **Color Palette:** Indigo (#4f46e5) primary + Slate grays
- **Typography:** Google Fonts (Outfit headings, Inter body)
- **Icons:** Phosphor Icons library (~40 icons used)
- **Accessibility:** Proper focus states, contrast ratios, icon+text pairs
- **Performance:** < 1s page load, ~10-50ms API response, ~46KB total frontend

---

## 🎯 Project Overview

**Objective:** Predict **Revenue** for e-commerce products based on pricing, discounts, and marketing spend using Random Forest Regressor with a professional, responsive web interface.

**Use Cases:**
- Forecast financial revenue
- Plan marketing budgets more effectively
- Optimize pricing and discount strategies
- Understand sales trends

---

## 📂 Project Structure

```
project/
├── data/
│   └── raw/                    # Original CSV dataset (1,000 e-commerce records)
├── src/
│   └── api/
│       └── app.py             # Flask REST API (3 endpoints: /, /status, /predict)
├── frontend/                   # Professional web frontend
│   ├── index.html             # HTML5 interface with Phosphor icons
│   ├── style.css              # CSS3 (755 lines) - Indigo theme, dark mode, responsive
│   └── script.js              # Vanilla JavaScript (322 lines) - Advanced features
├── models/                     # Trained model artifacts
│   ├── revenue_model.pkl       # Random Forest Regressor (300 trees)
│   ├── le_product.pkl         # Product category encoder
│   └── le_segment.pkl         # Customer segment encoder
├── notebooks/                  # Jupyter notebooks with analysis
├── app.py                      # Main Flask API entry point
├── train_model.py             # Model training script
├── Ecommerce_Sales_Prediction_Dataset.csv  # Training data
└── README.md                   # This file
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install flask flask-cors pandas scikit-learn joblib numpy requests
```

### 2. Train the Model (Optional - Model Pre-trained)
```bash
python train_model.py
```

Expected output:
- `models/revenue_model.pkl` - Trained Random Forest Regressor
- `models/le_product.pkl` - Product category encoder
- `models/le_segment.pkl` - Customer segment encoder

### 3. Start the API Backend
```bash
python app.py
```

The API will run on `http://localhost:5000`

### 4. Launch the Frontend
```bash
cd frontend
python -m http.server 8000
```

Open your browser: `http://localhost:8000`

---

## 📊 Dataset Information

**File:** `data/raw/Ecommerce_Sales_Prediction_Dataset.csv`
- **Size:** 1,000 records
- **Features:** 7 columns

| Column | Type | Description |
|--------|------|-------------|
| Date | DateTime | Sale date |
| Product_Category | Categorical | Electronics, Fashion, Home Decor, Sports, Toys |
| Price | Numeric | Product price |
| Discount | Numeric | Discount percentage (0-100) |
| Customer_Segment | Categorical | Premium, Regular, Occasional |
| Marketing_Spend | Numeric | Marketing budget |
| **Units_Sold** | **Numeric** | **Target variable** |

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor
- **Target Variable:** Revenue (Price × Units Sold)
- **Model Parameters:** 300 estimators
- **Train-Test Split:** 80%-20%
- **Training Data:** 1,000 e-commerce records

**Features Used for Prediction:**
1. Effective_Price (Price × (1 - Discount/100))
2. Discount (%)
3. Marketing_Spend
4. Day (date feature)
5. Month (date feature)

**Model Performance:**
- Mean Absolute Error (MAE): ~6.08 units
- Root Mean Squared Error (RMSE): ~7.70 units
- Handles non-linear relationships and feature interactions

**Key Architecture Decisions:**
- **Revenue-First:** The model predicts revenue directly from features.
- **Strict Validation:** Discounts must be between 0-100%. 100% discount results in 0 revenue.
- **Random Forest:** Provides better generalization than linear regression for complex relationships.

---

## 🔌 API Implementation Details

### Backend Architecture (`src/api/app.py`)
```python
# Model Loading
- Dynamically loads revenue_model.pkl from models/ directory
- Error handling for missing models with user-friendly messages
- Static initialization at startup

# Request Validation
- Required fields: Price, Discount, Marketing_Spend, Day, Month
- Type checking: All numeric values converted to float/int
- Business logic: Discount range 0-100%, 100% → $0 revenue

# Feature Engineering
- Effective_Price = Price × (1 - Discount/100)
- Features in training order: [Effective_Price, Discount, Marketing_Spend, Day, Month]
- Exact feature order matches training pipeline

# Response Format
- Status field: "success" or error message
- Predicted_revenue: Rounded to 2 decimal places
- Input echo: Returns submitted data for verification
```

### Endpoints

#### 1. Health Check
```bash
GET /
```
**Response:**
```json
{
  "status": "active",
  "service": "Revenue Prediction API",
  "model_loaded": true
}
```

#### 2. Model Status
```bash
GET /status
```
**Response:**
```json
{
  "status": "active",
  "model_loaded": true,
  "api_version": "1.0"
}
```

#### 3. Single Prediction
```bash
POST /predict
Content-Type: application/json

{
  "Price": 500.0,
  "Discount": 10.0,
  "Marketing_Spend": 1000.0,
  "Day": 15,
  "Month": 6
}
```

**Response:**
```json
{
  "status": "success",
  "predicted_revenue": 2450.75,
  "input": {
    "Price": 500.0,
    "Discount": 10.0,
    "Marketing_Spend": 1000.0,
    "Day": 15,
    "Month": 6
  }
}
```

**Error Response (Invalid Discount):**
```json
{
  "error": "Discount must be between 0 and 100"
}
```

**Error Response (Model Not Loaded):**
```json
{
  "error": "Model not loaded"
}
```

---

## 💻 Technology Stack

### Backend
| Component | Technology |
|-----------|-------------|
| **Language** | Python 3.12 |
| **Web Framework** | Flask 3.1.0 |
| **ML Library** | Scikit-learn 1.6.0 (Random Forest) |
| **Data Processing** | Pandas 2.2.3, NumPy 2.2.0 |
| **Serialization** | Joblib 1.4.2 |
| **Cross-Origin** | Flask-CORS |

### Frontend
| Component | Technology | Details |
|-----------|-------------|---------|
| **HTML** | HTML5 | Semantic markup, Phosphor icons |
| **CSS** | CSS3 (755 lines) | CSS variables, Indigo theme, dark mode, responsive grid |
| **JavaScript** | ES6+ (322 lines) | Vanilla JS, no frameworks, async/await |
| **Icons** | Phosphor Icons | Modern, accessible icon library |
| **Typography** | Google Fonts | Inter (body), Outfit (headings) |
| **Storage** | Browser LocalStorage | Persistent history & preferences |

---

## 📝 Code Architecture & Implementation

### Frontend JavaScript (322 lines, `frontend/script.js`)

**Configuration & State**
```javascript
const API_URL = 'http://localhost:5000';
const STORAGE_KEY = 'prediction_history';
const MAX_HISTORY = 20;  // Max history items
let predictionHistory = [];
let darkMode = localStorage.getItem('darkMode') === 'true';
```

**Core Functions**

1. **Initialization (`initializeApp`)**
   - Load history from localStorage
   - Setup event listeners
   - Check API status (10-second interval)
   - Apply saved dark mode preference

2. **Single Prediction (`handleSinglePrediction`)**
   - Form validation (discount 0-100%)
   - POST to `/predict` endpoint
   - Animated result display
   - Auto-add to history
   - Show input summary

3. **History Management**
   - `addToHistory()` - Add prediction to state
   - `updateHistoryDisplay()` - Render history items
   - `saveHistory()` - Persist to localStorage
   - `loadHistory()` - Restore on page load
   - `clearHistory()` - Confirmation-based deletion

4. **API Status (`checkAPIStatus`)**
   - Fetch `/status` endpoint every 10 seconds
   - Update status badge: connected/disconnected
   - Visual feedback with Phosphor icons

5. **Dark Mode (`toggleDarkMode`)**
   - Toggle class on body, containers, header
   - Persist preference to localStorage
   - Update all CSS variables

6. **CSV Export (`exportHistory`)**
   - Generate CSV with headers: Date, Product, Price, Prediction
   - Blob download with date-stamped filename
   - Format: `predictions_MM-DD-YYYY.csv`

7. **Validation & Utilities**
   - Form validation for price, discount, marketing spend
   - Category name mapping
   - Keyboard shortcut: Ctrl+Enter to submit
   - Error notifications

### Frontend CSS (755 lines, `frontend/style.css`)

**Theme System**
- Light mode: Slate (50-900) + Indigo (#4f46e5)
- Dark mode: Dark Slate (800-900) + Indigo (#6366f1)
- 50+ CSS custom properties for consistency

**Layout**
```css
.wrapper {
    grid-template-columns: 1.2fr 0.8fr;  /* 60-40 split */
    gap: 2rem;
}
@media (max-width: 900px) {
    grid-template-columns: 1fr;  /* Stack on mobile */
}
```

**Components**
- **Header:** Sticky, flexbox, status badge + dark mode toggle
- **Forms:** Enhanced inputs with Phosphor icon labels, focus rings
- **Buttons:** Gradient primary, flat secondary, outline tertiary
- **Cards:** 12px border radius, shadow-card elevation, border
- **Animations:** slideUp (0.4s), slideIn (0.3s), spin (0.8s)
- **Dark Mode:** Complete theme switch with proper contrast

**Responsive Breakpoints**
- Desktop: 1200px max-width, 2-column grid
- Tablet: 900px threshold, single column
- Mobile: 100% width, compact padding

### Frontend HTML (157 lines, `frontend/index.html`)

**Structure**
```html
<header>              <!-- Logo, API badge, dark toggle -->
<main>
  <left-column>      <!-- Prediction form + results -->
  <right-column>     <!-- Stats + history + export -->
</main>
```

**Key Elements**
- Phosphor Icons throughout (chart-polar, magic-wand, etc.)
- Google Fonts: Inter + Outfit
- Select dropdowns for categories & segments
- Number inputs with min/max/step validation
- Loading spinner + result display zones
- History list with timestamps
- Clear & export buttons

**Form Fields**
- Product Category (dropdown: 5 options)
- Price ($, 0+)
- Discount (%, 0-100)
- Customer Segment (dropdown: 3 options)
- Marketing Budget ($, 0+)

### Backend Python (`src/api/app.py`, 109 lines)

**Flask Setup**
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, numpy, os

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests
```

**Model Loading**
- Relative path: `../../models/revenue_model.pkl`
- Try/except with status message
- Model availability check before prediction

**Feature Engineering** (Exact notebook replication)
```python
effective_price = price * (1 - discount / 100)
features = np.array([[
    effective_price,
    discount,
    marketing_spend,
    day,
    month
]])
```

**Validation Logic**
- Discount range: 0-100%
- Special case: 100% discount → $0 revenue
- Type conversion safety: float/int parsing
- Error responses with proper HTTP codes (400, 500, 503)  

---

## 🔍 How to Use

### Frontend Workflow

**Step 1: Enter Product Details**
- Select Product Category (Electronics, Fashion, Home Decor, Sports, Toys)
- Enter Product Price ($)
- Set Discount Percentage (0-100%)
- Select Customer Segment (Premium, Regular, Occasional)
- Enter Marketing Budget ($)

**Step 2: Get Prediction**
- Click "Predict Sales" button (or Ctrl+Enter)
- Wait for API response (~500ms)
- View projected revenue in large display

**Step 3: Review Results**
- See input summary with breakdown
- Check API status indicator (top-right)
- View prediction in history automatically

**Step 4: Manage History**
- Click on history item to review
- Export all predictions to CSV
- Clear history with confirmation

**Step 5: Customize**
- Toggle dark mode (moon icon)
- Predictions persist across sessions
- History limited to 20 most recent

### Programmatic Usage (API)

**Python Example with Error Handling**
```python
import requests
from datetime import datetime

API_URL = "http://localhost:5000"

# Check API health
health = requests.get(f"{API_URL}/").json()
print(f"API Status: {health['status']}")

# Make prediction
now = datetime.now()
payload = {
    "Price": 500.0,
    "Discount": 10.0,
    "Marketing_Spend": 1000.0,
    "Day": now.day,
    "Month": now.month
}

try:
    response = requests.post(
        f"{API_URL}/predict",
        json=payload,
        timeout=5
    )
    result = response.json()
    
    if response.status_code == 200:
        print(f"✓ Predicted Revenue: ${result['predicted_revenue']:.2f}")
    else:
        print(f"✗ Error: {result['error']}")
except Exception as e:
    print(f"✗ Connection Error: {e}")
```

**cURL Example**
```bash
# Check API
curl http://localhost:5000/

# Get status
curl http://localhost:5000/status

# Make prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Price": 500.0,
    "Discount": 10.0,
    "Marketing_Spend": 1000.0,
    "Day": 15,
    "Month": 6
  }'
```

**JavaScript (Fetch API)**
```javascript
const payload = {
    Price: 500.0,
    Discount: 10.0,
    Marketing_Spend: 1000.0,
    Day: new Date().getDate(),
    Month: new Date().getMonth() + 1
};

fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
})
.then(r => r.json())
.then(data => console.log(`Revenue: $${data.predicted_revenue}`))
.catch(e => console.error('Error:', e));
```

---

## 🧪 Testing Guide

### Frontend Testing Checklist
- [ ] Form submission with valid data → Prediction appears
- [ ] Discount > 100% → Validation error message
- [ ] Discount = 100% → Revenue = $0.00
- [ ] API offline → "Connection Error" message
- [ ] Dark mode toggle → Theme switches completely
- [ ] Refresh page → History persists from localStorage
- [ ] Export CSV → File downloads with correct headers
- [ ] API status badge → Shows connected/disconnected
- [ ] Keyboard Ctrl+Enter → Submit form
- [ ] Mobile layout (< 900px) → Single column layout

### API Testing Checklist
- [ ] `curl http://localhost:5000/` → 200, active status
- [ ] `curl http://localhost:5000/status` → 200, model_loaded: true
- [ ] `POST /predict` valid data → 200, predicted_revenue returned
- [ ] `POST /predict` missing field → 400, error message
- [ ] `POST /predict` discount > 100 → 400, range error
- [ ] `POST /predict` discount = 100 → 200, revenue = 0.0
- [ ] Model missing → 503, "Model not loaded"
- [ ] Response time < 100ms → Performance acceptable

### Load Testing
```bash
# Simple sequential test
for i in {1..10}; do
  curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"Price":500,"Discount":10,"Marketing_Spend":1000,"Day":15,"Month":6}'
done

# Parallel test (if stress-testing needed)
parallel curl -X POST http://localhost:5000/predict ... ::: {1..20}
```

---

## 📚 Jupyter Notebooks

The project includes Jupyter notebooks with detailed analysis and exploration:
- `Airbnb_Project.ipynb` - E-commerce sales prediction with Random Forest implementation
- `Forecasting_Property_Prices_Using_Regression_Techniques.ipynb` - Reference analysis

---

## 🛠️ Development Notes

**Model Retraining:**
```bash
python train_model.py
```

**Known Limitations:**
- Discount must be between 0-100%
- 100% discount results in 0 revenue
- All inputs are required for prediction

---

## 🎨 Frontend Features & Implementation

### Design System
- **Color Scheme:** Indigo primary (#4f46e5) with complementary Slate grays
- **Theme Variables:** 50+ CSS custom properties for consistency
- **Dark Mode:** Full theme switch with localStorage persistence
- **Responsive:** Grid: 1.2fr 0.8fr (desktop) → 1fr (mobile at 900px)
- **Typography:** Outfit for headings, Inter for body (Google Fonts)
- **Icons:** Phosphor Icons (~40 icons throughout interface)

### UI Components
- **Header:** Logo, API status badge, dark mode toggle (sticky)
- **Status Badge:** Real-time API connection indicator (connected/disconnected)
- **Form Controls:** Enhanced inputs with icon labels, validation feedback
- **Results Display:** Animated reveal with success/error states
- **History:** 20-item limit, auto-saves to localStorage, sortable by timestamp
- **Stats Cards:** Total predictions and last update displays
- **Loading State:** Animated spinner with context message

### Advanced Functionality
✅ **Single Predictions** - Real-time form validation and API integration  
✅ **Dark Mode Toggle** - Persistent preference with full CSS coverage  
✅ **History Tracking** - Automatic localStorage with 20-item limit  
✅ **CSV Export** - Download predictions in standard format with date stamping  
✅ **API Status Monitoring** - 10-second check interval with visual indicators  
✅ **Input Validation** - Discount range (0-100%), numeric checks  
✅ **Keyboard Shortcuts** - Ctrl+Enter to submit form  
✅ **Error Handling** - User-friendly messages for connection/validation errors  
✅ **Responsive Layout** - Mobile-first with adaptive grid at 900px breakpoint  

## 🎨 Frontend Features & Implementation

### Design System
- **Color Scheme:** Indigo primary (#4f46e5) with complementary Slate grays
- **Theme Variables:** 50+ CSS custom properties for consistency
- **Dark Mode:** Full theme switch with localStorage persistence
- **Responsive:** Grid: 1.2fr 0.8fr (desktop) → 1fr (mobile at 900px)
- **Typography:** Outfit for headings, Inter for body (Google Fonts)
- **Icons:** Phosphor Icons (~40 icons throughout interface)

### UI Components
- **Header:** Logo, API status badge, dark mode toggle (sticky)
- **Status Badge:** Real-time API connection indicator (connected/disconnected)
- **Form Controls:** Enhanced inputs with icon labels, validation feedback
- **Results Display:** Animated reveal with success/error states
- **History:** 20-item limit, auto-saves to localStorage, sortable by timestamp
- **Stats Cards:** Total predictions and last update displays
- **Loading State:** Animated spinner with context message

### Advanced Functionality
✅ **Single Predictions** - Real-time form validation and API integration  
✅ **Dark Mode Toggle** - Persistent preference with full CSS coverage  
✅ **History Tracking** - Automatic localStorage with 20-item limit  
✅ **CSV Export** - Download predictions in standard format with date stamping  
✅ **API Status Monitoring** - 10-second check interval with visual indicators  
✅ **Input Validation** - Discount range (0-100%), numeric checks  
✅ **Keyboard Shortcuts** - Ctrl+Enter to submit form  
✅ **Error Handling** - User-friendly messages for connection/validation errors  
✅ **Responsive Layout** - Mobile-first with adaptive grid at 900px breakpoint  

### CSS Architecture (755 lines)
- **Variables System:** Light & dark mode themes with 50+ custom properties
- **Layout:** CSS Grid for responsive 2-column layout
- **Forms:** Enhanced inputs with focus rings and transitions
- **Animations:** slideUp (results), slideIn (notifications), spin (loader)
- **Dark Mode:** Complete theme switch with accent color adaptation
- **Accessibility:** Focus states, proper contrast, icon-text pairings

## 🎓 Learning Outcomes

This project demonstrates:
1. **End-to-End ML Pipeline** - Data loading, preprocessing, feature engineering, training
2. **Model Selection** - Random Forest with hyperparameter tuning
3. **REST API Development** - Flask with validation and error handling
4. **Responsive Web Design** - Mobile-first CSS without frameworks
5. **Frontend Development** - Vanilla JavaScript with advanced features
6. **Best Practices** - Project organization, separation of concerns
7. **User Experience** - Dark mode, history tracking, data export

---

## 📞 Troubleshooting

**API Not Running:**
```bash
python app.py
```

**Frontend Not Loading:**
```bash
cd frontend && python -m http.server 8000
```

**Predictions Not Working:**
1. Verify API running: `curl http://localhost:5000/`
2. Check browser console (F12)
3. Ensure discount is 0-100

**Models Missing:**
Run `python train_model.py`

---

---

## 📞 Troubleshooting

**API Not Running:**
```bash
python app.py
```

**Frontend Not Loading:**
```bash
cd frontend && python -m http.server 8000
```

**Predictions Not Working:**
1. Verify API running: `curl http://localhost:5000/`
2. Check browser console (F12)
3. Ensure discount is 0-100

**Models Missing:**
Run `python train_model.py`

---

## 📊 File Size & Performance

| File | Size | Lines | Purpose |
|------|------|-------|---------|
| `frontend/index.html` | ~6KB | 157 | Semantic HTML5 structure |
| `frontend/style.css` | ~30KB | 755 | Complete styling + dark mode |
| `frontend/script.js` | ~10KB | 322 | All frontend functionality |
| `src/api/app.py` | ~3KB | 109 | Flask REST API |
| `models/revenue_model.pkl` | ~19MB | - | Random Forest model (300 trees) |
| **Total Frontend** | **~46KB** | **1,234** | **Production-ready** |

**Performance Metrics**
- API Response Time: ~10-50ms (prediction)
- Page Load Time: < 1 second
- History Query: < 10ms (localStorage)
- CSS Coverage: 100% light + dark mode
- JavaScript: No external dependencies except Phosphor Icons CDN

## 🔐 Security & Best Practices

**API Security**
- CORS enabled for frontend integration
- Input validation on all fields
- Type conversion with error handling
- HTTP status codes follow REST conventions
- No sensitive data in responses

**Frontend Security**
- No sensitive data stored in localStorage
- History data is local-only (never sent to server)
- Form validation before submission
- Keyboard shortcuts scoped to form context
- Error messages don't expose system details

**Data Handling**
- All numeric inputs validated (type, range)
- Discount range strictly 0-100%
- Special handling for edge case (100% discount → $0)
- No SQL/database (flat model files)
- CSV export is client-side only

---

**Last Updated:** December 13, 2025  
**Status:** ✅ Production Ready  
**Version:** 2.0 (Complete: Random Forest ML + Professional Frontend)  

## 👨‍🎓 Author
This project was developed as part of the **Forecast & Predictive Analytics** course.
