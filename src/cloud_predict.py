import requests

url = "https://online-shopper-intention-fastapi.onrender.com/predict"

sample = {
    "administrative": 0,
    "administrative_duration": 0.0,
    "informational": 0,
    "informational_duration": 0.0,
    "product_related": 4,
    "product_related_duration": 104.0,
    "bounce_rates": 0.0,
    "exit_rates": 0.05,
    "page_values": 0.0,
    "special_day": 0.0,
    "month": "May",
    "operating_systems": "2",
    "browser": "10",
    "region": "2",
    "traffic_type": "2",
    "visitor_type": "returning_visitor",
    "weekend": 0
}

response = requests.post(url, json=sample)
print(response.json())

# To run:
# python src/cloud_predict.py