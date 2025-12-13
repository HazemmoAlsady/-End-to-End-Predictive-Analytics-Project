import urllib.request
import json
import urllib.error

url = 'http://localhost:5000/predict'
data = {
    "Product_Category": "Electronics",
    "Price": 100,
    "Discount": 10,
    "Customer_Segment": "Regular",
    "Marketing_Spend": 1000
}

headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status Code: {response.getcode()}")
        print("Response Text:")
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
