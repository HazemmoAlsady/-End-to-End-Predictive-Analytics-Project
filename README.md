# 📊 E-Commerce Sales Prediction

Advanced ML forecasting system with REST API and professional web frontend for predicting e-commerce revenue.

**Objective:** Predict revenue based on pricing, discounts, and marketing spend using Random Forest Regressor.

---

## 📂 Project Structure

```
├── app.py                      # Flask REST API (3 endpoints)
├── train_model.py             # Model training script
├── requirements.txt           # Python dependencies
├── models/                    # Trained artifacts
│   ├── revenue_model.pkl      # Random Forest (300 trees)
│   ├── le_product.pkl         # Category encoder
│   └── le_segment.pkl         # Segment encoder
├── frontend/
│   ├── index.html             # UI (157 lines)
│   ├── style.css              # Styling (755 lines, dark mode)
│   └── script.js              # Logic (322 lines)
├── Ecommerce_Sales_Prediction_Dataset.csv
└── notebooks/                 # Analysis notebooks
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install flask flask-cors pandas scikit-learn joblib

# 2. Train model (optional - pre-trained)
python train_model.py

# 3. Start API
python app.py

# 4. Launch frontend
cd frontend && python -m http.server 8000
```

Access: `http://localhost:8000`

---

## 📊 Dataset

1,000 e-commerce records with 5 input features:

| Feature | Type | Notes |
|---------|------|-------|
| Product_Category | Categorical | Electronics, Fashion, Home, Sports, Toys |
| Price | Numeric | Product price |
| Discount | Numeric | 0-100% |
| Customer_Segment | Categorical | Premium, Regular, Occasional |
| Marketing_Spend | Numeric | Budget spent |

**Target:** Revenue (Price × Units Sold)

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor  
**Estimators:** 300 trees  
**Performance:** MAE ~6.08, RMSE ~7.70  
**Features:** Effective_Price, Discount, Marketing_Spend, Day, Month

---

## 🔌 API Endpoints

### GET /
Health check
```json
{"status": "active", "service": "Revenue Prediction API", "model_loaded": true}
```

### GET /status
Model status
```json
{"status": "active", "model_loaded": true, "api_version": "1.0"}
```

### POST /predict
Predict revenue
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"Price":500,"Discount":10,"Marketing_Spend":1000,"Day":15,"Month":6}'
```

Response:
```json
{
  "status": "success",
  "predicted_revenue": 2450.75,
  "input": {"Price": 500.0, "Discount": 10.0, "Marketing_Spend": 1000.0, "Day": 15, "Month": 6}
}
```

---

## 💻 Technology Stack

| Component | Technology |
|-----------|-------------|
| **Backend** | Python 3.12, Flask 3.1.0, Scikit-learn 1.6.0 |
| **Frontend** | HTML5, CSS3 (755 lines), Vanilla JavaScript (322 lines) |
| **ML Model** | Random Forest (300 trees), Joblib serialization |
| **Icons** | Phosphor Icons (~40 used) |
| **Typography** | Google Fonts (Outfit, Inter) |
| **Storage** | Browser LocalStorage |

---

## ✨ Frontend Features

✅ Real-time predictions with form validation  
✅ Dark mode toggle (localStorage persistence)  
✅ Prediction history (20-item limit)  
✅ CSV export with timestamps  
✅ API status monitoring  
✅ Responsive grid layout (1.2fr/0.8fr → 1fr at 900px)  
✅ Indigo theme (#4f46e5) + Slate grays  
✅ Keyboard shortcuts (Ctrl+Enter)  
✅ Error handling & accessibility

---

## 🧪 Testing

**Frontend:**
- Form submission with valid data → Prediction appears ✓
- Discount > 100% → Validation error ✓
- Dark mode toggle → Theme switches ✓
- Refresh page → History persists ✓
- Mobile layout (< 900px) → Single column ✓

**API:**
- `GET /` → 200 status ✓
- `POST /predict` with valid data → Prediction ✓
- Invalid discount → 400 error ✓
- Discount = 100 → Revenue = $0.00 ✓

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| API not running | `python app.py` |
| Frontend not loading | `cd frontend && python -m http.server 8000` |
| Models missing | `python train_model.py` |
| Predictions failing | Check API status: `curl http://localhost:5000/` |
| Discount validation error | Ensure discount is 0-100 |

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| Frontend Size | ~46KB (1,234 lines) |
| Backend Size | ~3KB (109 lines) |
| Page Load | < 1 second |
| API Response | 10-50ms |
| Model Size | 19MB |
| Training Data | 1,000 records (80-20 split) |
| Browser Support | All modern browsers |

---

## 🔐 Security

- CORS enabled for frontend integration
- All numeric inputs validated (type, range)
- Discount strictly 0-100%
- No sensitive data in localStorage
- History is local-only
- Error messages are user-friendly

---

**Status:** ✅ Production Ready  
**Version:** 2.0  
**Last Updated:** December 13, 2025
