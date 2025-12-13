# 📊 E-Commerce Units Sales Prediction - Revenue Analytics

A complete **end-to-end predictive analytics project** with REST API for predicting e-commerce sales units using machine learning.

---

## 🎯 Project Overview

**Objective:** Predict the number of units sold for e-commerce products based on pricing, discounts, customer behavior, and marketing spend.

**Use Cases:**
- Forecast inventory requirements
- Plan marketing budgets more effectively
- Optimize pricing strategies
- Predict revenue based on sales volumes

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

### 2. Train the Model
```bash
cd src/models
python train.py
```

Expected output:
- `revenue_model.pkl` - Trained Random Forest model
- `le_product.pkl` - Product category encoder
- `le_segment.pkl` - Customer segment encoder

### 3. Start the API
```bash
python src/api/app.py
```

The API will run on `http://localhost:5000`

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
- **Number of Trees:** 300
- **Train-Test Split:** 80%-20%
- **Random State:** 42

**Features Used for Prediction:**
1. Effective_Price (Price × (1 - Discount/100))
2. Discount
3. Marketing_Spend
4. Day (extracted from date)
5. Month (extracted from date)

**Performance Metrics:**
- MAE: 6.08 units
- RMSE: 7.70 units
- R² Score: -0.096 (indicates simple linear relationship)

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

### 3. Single Prediction
```bash
POST /predict
Content-Type: application/json

{
  "Product_Category": "Electronics",
  "Price": 500.0,
  "Discount": 10.0,
  "Customer_Segment": "Premium",
  "Marketing_Spend": 1000.0
}
```

**Response:**
```json
{
  "status": "success",
  "predicted_units_sold": 27.36,
  "input": {...}
}
```

### 4. Batch Predictions
```bash
POST /predict/batch
Content-Type: application/json

{
  "records": [
    {
      "Product_Category": "Electronics",
      "Price": 500.0,
      "Discount": 10.0,
      "Customer_Segment": "Premium",
      "Marketing_Spend": 1000.0
    }
  ]
}
```

---

## 💻 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.12 |
| **Web Framework** | Flask 3.1.0 |
| **ML Library** | Scikit-learn 1.6.0 |
| **Data Processing** | Pandas 2.2.3, NumPy 2.2.0 |
| **Serialization** | Joblib 1.4.2 |
| **CORS** | Flask-CORS |
| **Testing** | Requests library |

---

## 📝 Key Features

✅ **Random Forest Model** - Better generalization than linear regression  
✅ **Feature Engineering** - Effective price calculation, date extraction  
✅ **REST API** - 4 production-ready endpoints with error handling  
✅ **Input Validation** - Comprehensive validation on all inputs  
✅ **CORS Support** - Enable cross-origin requests from web frontends  
✅ **Logging** - Track model training and API requests  
✅ **Batch Processing** - Predict multiple records at once  
✅ **Artifact Management** - Organized model storage and loading  

---

## 🔍 How to Use the API

### Python Example
```python
import requests
import json

url = "http://localhost:5000/predict"
payload = {
    "Product_Category": "Electronics",
    "Price": 500.0,
    "Discount": 10.0,
    "Customer_Segment": "Premium",
    "Marketing_Spend": 1000.0
}

response = requests.post(url, json=payload)
result = response.json()
print(f"Predicted units: {result['predicted_units_sold']}")
```

### cURL Example
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Product_Category": "Electronics",
    "Price": 500.0,
    "Discount": 10.0,
    "Customer_Segment": "Premium",
    "Marketing_Spend": 1000.0
  }'
```

---

## 🧪 Testing

Run the test suite:
```bash
python tests/test_api.py
```

Tests cover:
- Health check endpoint
- Status endpoint
- Single prediction
- Batch predictions

---

## 📚 Notebooks

The project includes two Jupyter notebooks with detailed analysis:
- `Airbnb_Project.ipynb` - E-commerce sales prediction analysis
- `Forecasting_Property_Prices_Using_Regression_Techniques.ipynb` - Real estate forecasting reference

---

## 🛠️ Development Notes

**Model Retraining:**
```bash
python src/models/train.py
```

**View Logs:**
```bash
tail -f logs/api.log
```

**Known Limitations:**
- R² score is negative, indicating the model might be better served with feature engineering
- Categories must match trained encoders (Electronics, Fashion, Home Decor, Sports, Toys)
- Date parameter is optional; current date used if not provided

---

## 📋 Configuration

All configuration in `config/`:
- `.env` - Environment variables
- `config.py` - API settings
- `model_config.py` - Model constants

---

## 🎓 Learning Outcomes

This project demonstrates:
1. **Data Pipeline** - Loading, preprocessing, feature engineering
2. **Model Selection** - Comparing multiple algorithms (Linear Regression vs Random Forest)
3. **Production Deployment** - REST API with Flask
4. **Best Practices** - Project organization, error handling, logging
5. **ML Workflow** - Training, evaluation, serialization, deployment

---

## 📞 Support

For issues or questions:
1. Check API logs in `logs/api.log`
2. Verify models are trained: `ls models/*.pkl`
3. Test API health: `curl http://localhost:5000/`

---

**Last Updated:** December 13, 2025  
**Status:** ✅ Production Ready
---

## 👨‍🎓 Author
This project was developed as part of the **Forecast & Predictive Analytics** course.
