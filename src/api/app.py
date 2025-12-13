from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '../../models')
MODEL_PATH = os.path.join(MODEL_DIR, 'revenue_model.pkl')

# Load model
model = None
try:
    model = joblib.load(MODEL_PATH)
    print("✓ Revenue model loaded successfully")
except Exception as e:
    print("✗ Failed to load model:", str(e))


@app.route('/')
def health_check():
    return jsonify({
        "status": "active",
        "service": "Revenue Prediction API",
        "model_loaded": model is not None
    })


@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 503

    try:
        data = request.get_json()

        # Required inputs 
        required_fields = ['Price', 'Discount', 'Marketing_Spend', 'Day', 'Month']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Parse inputs
        price = float(data['Price'])
        discount = float(data['Discount'])
        marketing_spend = float(data['Marketing_Spend'])
        
        # Validation
        if not (0 <= discount <= 100):
            return jsonify({"error": "Discount must be between 0 and 100"}), 400

        # Special Case: 100% Discount -> 0 Revenue
        if discount == 100:
             return jsonify({
                "status": "success",
                "predicted_revenue": 0.0,
                "input": data
            })
        day = int(data['Day'])
        month = int(data['Month'])

        # Feature Engineering (EXACTLY LIKE NOTEBOOK)
        effective_price = price * (1 - discount / 100)

        # Feature order MUST match training
        # ['Effective_Price', 'Discount', 'Marketing_Spend', 'Day', 'Month']
        features = np.array([[
            effective_price,
            discount,
            marketing_spend,
            day,
            month
        ]])

        # Prediction (Target = Revenue)
        predicted_revenue = model.predict(features)[0]

        return jsonify({
            "status": "success",
            "predicted_revenue": round(float(predicted_revenue), 2),
            "input": {
                "Price": price,
                "Discount": discount,
                "Marketing_Spend": marketing_spend,
                "Day": day,
                "Month": month
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "active",
        "model_loaded": model is not None,
        "api_version": "1.0"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
