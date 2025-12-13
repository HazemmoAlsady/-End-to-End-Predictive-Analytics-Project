"""API Test Suite"""
import requests
import json
from pprint import pprint

BASE_URL = 'http://localhost:5000'

def test_home():
    print("\n" + "="*60)
    print("TEST 1: Home Endpoint (GET /)")
    print("="*60)
    try:
        response = requests.get(f'{BASE_URL}/')
        print(f"Status: {response.status_code}")
        pprint(response.json())
    except Exception as e:
        print(f"Error: {e}")

def test_status():
    print("\n" + "="*60)
    print("TEST 2: Status Endpoint (GET /status)")
    print("="*60)
    try:
        response = requests.get(f'{BASE_URL}/status')
        print(f"Status: {response.status_code}")
        pprint(response.json())
    except Exception as e:
        print(f"Error: {e}")

def test_predict():
    print("\n" + "="*60)
    print("TEST 3: Single Prediction (POST /predict)")
    print("="*60)
    
    payload = {
        'Product_Category': 'Electronics',
        'Price': 500.0,
        'Discount': 10.0,
        'Customer_Segment': 'Premium',
        'Marketing_Spend': 1000.0
    }
    
    print("Payload:", json.dumps(payload, indent=2))
    
    try:
        response = requests.post(f'{BASE_URL}/predict', json=payload)
        print(f"Status: {response.status_code}")
        pprint(response.json())
    except Exception as e:
        print(f"Error: {e}")

def test_batch():
    print("\n" + "="*60)
    print("TEST 4: Batch Prediction (POST /predict/batch)")
    print("="*60)
    
    payload = [
        {
            'Product_Category': 'Electronics',
            'Price': 500.0,
            'Discount': 10.0,
            'Customer_Segment': 'Premium',
            'Marketing_Spend': 1000.0
        },
        {
            'Product_Category': 'Clothing',
            'Price': 100.0,
            'Discount': 20.0,
            'Customer_Segment': 'Regular',
            'Marketing_Spend': 500.0
        }
    ]
    
    print(f"Records: {len(payload)}")
    
    try:
        response = requests.post(f'{BASE_URL}/predict/batch', json=payload)
        print(f"Status: {response.status_code}")
        pprint(response.json())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("\n" + "█"*60)
    print("   Revenue Prediction API - Test Suite")
    print("█"*60)
    
    try:
        test_home()
        test_status()
        test_predict()
        test_batch()
        
        print("\n" + "="*60)
        print("✓ All tests completed!")
        print("="*60 + "\n")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to API")
        print("Run: D:\\Python\\python.exe src/api/app.py\n")
