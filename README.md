# 📊 E-Commerce Sales Prediction - Advanced ML Forecasting System

A complete **end-to-end predictive analytics project** with REST API and professional web frontend for predicting e-commerce revenue using machine learning.

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
│   ├── raw/                    # Original CSV dataset
│   └── processed/              # Processed data (if needed)
├── src/
│   ├── api/
│   │   └── app.py             # Flask REST API (4 endpoints)
│   └── models/
│       └── train.py           # Model training script
├── models/                     # Trained model artifacts (.pkl files)
├── notebooks/                  # Jupyter notebooks (original analysis)
├── tests/                      # API test suite
├── config/                     # Configuration files
├── logs/                       # Application logs
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

## 🔌 API Endpoints

### 1. Health Check
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

### 2. Model Status
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

### 3. Single Prediction
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

---

## 💻 Technology Stack

### Backend
| Component | Technology |
|-----------|-------------|
| **Language** | Python 3.12 |
| **Web Framework** | Flask 3.1.0 |
| **ML Library** | Scikit-learn 1.6.0 |
| **Data Processing** | Pandas 2.2.3, NumPy 2.2.0 |
| **Serialization** | Joblib 1.4.2 |
| **API Security** | Flask-CORS |

### Frontend
| Component | Technology |
|-----------|-------------|
| **Markup** | HTML5 |
| **Styling** | CSS3 (Vanilla, No Framework) |
| **Scripting** | Vanilla JavaScript ES6+ |
| **Icons** | Phosphor Icons |
| **Fonts** | Google Fonts (Inter, Outfit) |
| **Storage** | Browser LocalStorage |

---

## 📝 Key Features

### Backend
✅ **Random Forest Regressor** - Advanced ML model with better generalization  
✅ **Revenue Prediction** - Direct forecast of financial outcomes  
✅ **REST API** - Streamlined endpoints with input validation  
✅ **Strict Validation** - Discount range checking (0-100%)  
✅ **CORS Support** - Enable cross-origin requests from web frontends  
✅ **Artifact Management** - Organized model storage and loading  

### Frontend
✅ **Professional UI** - Modern, clean design with solid colors (no gradients)  
✅ **Fully Responsive** - Optimized for mobile, tablet, and desktop  
✅ **Dark Mode** - Toggle between light and dark themes  
✅ **History Tracking** - Automatic history with localStorage persistence  
✅ **Batch Predictions** - Submit multiple predictions at once  
✅ **CSV Export** - Download prediction results as CSV file  
✅ **Real-time API Status** - Monitor API connection status  
✅ **English Language** - Professional English text throughout  

---

## 🔍 How to Use

### Via Web Frontend
1. Open `http://localhost:8000` in your browser
2. Enter product details
3. Click "Predict" to see the revenue forecast
4. View prediction history automatically saved
5. Export results to CSV anytime

### Via API (Python Example)
```python
import requests
from datetime import datetime

url = "http://localhost:5000/predict"
now = datetime.now()

payload = {
    "Price": 500.0,
    "Discount": 10.0,
    "Marketing_Spend": 1000.0,
    "Day": now.day,
    "Month": now.month
}

response = requests.post(url, json=payload)
result = response.json()
print(f"Predicted Revenue: ${result['predicted_revenue']:.2f}")
```

### Via cURL
```bash
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

---

## 🧪 Testing the API

### Quick API Test
```bash
curl http://localhost:5000/
```

Should return status 200 with active message.

### Frontend Testing
1. Open `http://localhost:8000`
2. Test single prediction form
3. Verify dark mode toggle
4. Check history persistence
5. Export predictions to CSV

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

## 🎨 Frontend Features

### UI/UX
- **Color Scheme:** Professional blue (#3b82f6) with solid colors
- **No Gradients:** Clean, readable design
- **Responsive Grid:** 2-column desktop → 1-column mobile
- **Dark Mode:** Toggle with persistent preference
- **Animations:** Smooth transitions and interactions

### Functionality
- **Single Predictions:** One prediction at a time
- **Batch Predictions:** Multiple predictions at once
- **History Management:** Automatic tracking
- **CSV Export:** Download results
- **API Status:** Real-time monitoring

---

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

**Last Updated:** December 13, 2025  
**Status:** ✅ Production Ready  
**Version:** 2.0 (Random Forest + Professional Frontend)  
