import requests as req
import time

valid_token = "abc123"
invalid_token = "123abc"

data = {
    "age": 42,
    "job": "entrepreneur",
    "marital": "married",
    "education": "primary",
    "balance": 558,
    "housing": "yes",
    "duration": 186,
    "campaign": 2,
}

print("Test if API is alive...")
resp = req.get("http://localhost:8900/")
print(f"Status code: {resp.status_code}")
print(f"Server Response: {resp.text}")
print()

print("Test prediction endpoint with valid token...")
headers = {"Authorization": f"Bearer {valid_token}"}
resp = req.post("http://localhost:8900/predict",
                json=data,
                headers=headers)
print(f"Status code: {resp.status_code}")
print(f"Server Response: {resp.text}")
print()

print("Test prediction endpoint with invalid token...")
headers = {"Authorization": f"Bearer {invalid_token}"}
resp = req.post("http://localhost:8900/predict",
                json=data,
                headers=headers)
print(f"Status code: {resp.status_code}")
print(f"Server Response: {resp.text}")
print()

