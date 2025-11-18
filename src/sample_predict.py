from model import load_model, predict_single

dv, model = load_model()

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

print("Prediction:", predict_single(sample, dv, model))

# To run:
# python src/sample_predict.py