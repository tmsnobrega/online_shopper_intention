🛍️ Online Shopper Purchase Intention — ML Model & FastAPI Deployment

This project predicts whether an online user will make a purchase based on their browsing session data.
It includes:

Full EDA

Model development (Logistic Regression, Random Forest, XGBoost)

Model comparison

Final deployment using FastAPI + Docker

📊 1. Project Overview

The goal is to predict whether a user session will result in a purchase (Revenue = 1) using behavioral and engagement metrics from online shopping activity.

Models tested:

Logistic Regression

Random Forest

XGBoost (final deployed model)

The final model (XGBoost) is deployed as a FastAPI web service running inside Docker.

📂 2. Project Structure
.
├── models/
│   ├── xgboost_model.pkl
│   └── random_forest.pkl
│
├── src/
│   ├── app.py               # FastAPI app
│   ├── model.py             # Model loading & prediction logic
│   ├── __init__.py
│
├── notebooks/
│   └── training.ipynb       # EDA + model training
│
├── uv.lock
├── pyproject.toml
├── Dockerfile
├── predict.py               # API test client
└── README.md

📈 3. Model Performance Summary
Model	ROC AUC	Precision	Recall	F1 Score
Logistic Regression	0.910	0.707	0.365	0.481
Random Forest	0.935	0.811	0.476	0.600
XGBoost (Final Model)	0.938	0.718	0.595	0.651

XGBoost consistently provided:

highest ROC AUC

highest recall

highest F1-score

strongest balance across confusion matrix metrics

Therefore, XGBoost was selected for deployment.

⚙️ 4. Running the API Locally (Without Docker)
1. Start virtual environment
source .venv/Scripts/activate

2. Run FastAPI server
uvicorn src.app:app --reload

Open docs:
http://localhost:8000/docs

🐳 5. Running the API with Docker
1. Build Docker image
docker build -t shopper-intent .

2. Run the container
docker run -p 8000:8000 shopper-intent

Open the interactive API:
http://localhost:8000/docs

📡 6. Example POST Request

Using predict.py:

import requests

url = "http://localhost:8000/predict"

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

print(requests.post(url, json=sample).json())


or via curl:

curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"administrative":0, "administrative_duration":0.0, ... }'

🧠 7. Key EDA Insights

Only ~15% of sessions convert → strong class imbalance

Higher engagement (PageValues, ProductRelated) strongly predicts purchase

High ExitRates & BounceRates indicate non-buying behavior

New visitors convert more than returning visitors

Strong seasonal effects (peak in November)

Most predictive categorical features: month, traffic_type

Rarer categories were grouped into "other" to stabilize estimates

🚀 8. Deployment Notes
✔️ Uses FastAPI
✔️ Packaged with Docker
✔️ Dependencies managed with uv + uv.lock
✔️ Model loaded via DictVectorizer + XGBoost
✔️ API production-ready
🎉 9. Final Notes

This project demonstrates the full lifecycle of an ML model:

Data cleaning

EDA

Feature engineering

Modeling

Evaluation

Model comparison

Deployment with FastAPI

Containerization with Docker

You now have a ready-to-ship inference service.