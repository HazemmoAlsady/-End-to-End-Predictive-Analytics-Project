from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for frontend integration

# Model Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '../../models')

model_path = os.path.join(MODEL_DIR, 'revenue_model.pkl')
le_product_path = os.path.join(MODEL_DIR, 'le_product.pkl')
le_segment_path = os.path.join(MODEL_DIR, 'le_segment.pkl')

# Load Artifacts
model = None
le_product = None
le_segment = None

def load_artifacts():
    global model, le_product, le_segment
    try:
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            le_product = joblib.load(le_product_path)
            le_segment = joblib.load(le_segment_path)
            print("✓ Models loaded successfully from:", MODEL_DIR)
        else:
            print(f"⚠ Artifacts not found in {MODEL_DIR}. Please run src/models/train.py first.")
    except Exception as e:
        print(f"Error loading models: {str(e)}")

# Load on startup
load_artifacts()

@app.route('/')
def health_check():
    return jsonify({
        "status": "active",
        "service": "Revenue Prediction API",
        "model_loaded": model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded"}), 503

    try:
        from datetime import datetime
        data = request.get_json()
        
        # Validating input
        required_fields = ['Product_Category', 'Price', 'Discount', 'Customer_Segment', 'Marketing_Spend']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Extract Price and Discount for Effective Price calculation
        price = float(data['Price'])
        discount = float(data['Discount'])
        effective_price = price * (1 - discount / 100)
        
        # Get day and month (using current date if not provided)
        if 'Date' in data:
            try:
                date = datetime.strptime(data['Date'], '%d-%m-%Y')
                day = date.day
                month = date.month
            except:
                day = datetime.now().day
                month = datetime.now().month
        else:
            day = datetime.now().day
            month = datetime.now().month
        
        marketing_spend = float(data['Marketing_Spend'])
        
        # Prepare features for prediction (matching train.py feature order)
        # Features: ['Effective_Price', 'Discount', 'Marketing_Spend', 'Day', 'Month']
        features = np.array([[
            effective_price,
            discount,
            marketing_spend,
            day,
            month
        ]])
        
        # Predict
        prediction = model.predict(features)[0]
        
        return jsonify({
            "status": "success",
            "predicted_units_sold": round(float(prediction), 2),
            "input": {
                "Product_Category": data['Product_Category'],
                "Price": price,
                "Discount": discount,
                "Customer_Segment": data['Customer_Segment'],
                "Marketing_Spend": marketing_spend,
                "Date": f"{day:02d}-{month:02d}-2024"
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    if not model:
        return jsonify({"error": "Model not loaded"}), 503

    try:
        from datetime import datetime
        data = request.get_json()
        
        if 'records' not in data or not isinstance(data['records'], list):
            return jsonify({"error": "Missing 'records' array"}), 400

        results = []
        
        for record in data['records']:
            # Validating input
            required_fields = ['Product_Category', 'Price', 'Discount', 'Customer_Segment', 'Marketing_Spend']
            if not all(field in record for field in required_fields):
                return jsonify({"error": f"Missing required fields in record"}), 400

            # Extract Price and Discount for Effective Price calculation
            price = float(record['Price'])
            discount = float(record['Discount'])
            effective_price = price * (1 - discount / 100)
            
            # Get day and month (using current date if not provided)
            if 'Date' in record:
                try:
                    date = datetime.strptime(record['Date'], '%d-%m-%Y')
                    day = date.day
                    month = date.month
                except:
                    day = datetime.now().day
                    month = datetime.now().month
            else:
                day = datetime.now().day
                month = datetime.now().month
            
            marketing_spend = float(record['Marketing_Spend'])
            
            # Prepare features for prediction
            features = np.array([[
                effective_price,
                discount,
                marketing_spend,
                day,
                month
            ]])
            
            # Predict
            prediction = model.predict(features)[0]
            
            results.append({
                "product_category": record['Product_Category'],
                "price": price,
                "discount": discount,
                "customer_segment": record['Customer_Segment'],
                "marketing_spend": marketing_spend,
                "predicted_units_sold": round(float(prediction), 2)
            })
        
        return jsonify({
            "status": "success",
            "total_records": len(results),
            "predictions": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "active",
        "model_loaded": model is not None,
        "model_path": MODEL_DIR,
        "api_version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
