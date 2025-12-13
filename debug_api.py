import requests
import json

url = 'http://localhost:5000/predict'
data = {
    "Product_Category": "Electronics",
    "Price": 100,
    "Discount": 10,
    "Customer_Segment": "Regular",
    "Marketing_Spend": 1000
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response Text:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
