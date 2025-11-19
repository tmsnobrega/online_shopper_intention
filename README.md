
# **🛍️ Online Shopper Purchase Intention**

**Binary Classification • Machine Learning • XGBoost • FastAPI • Docker • Cloud Deployment**

This project answers a key business question: “Will this visitor make a purchase?”

Using user behavior data, it demonstrates the complete machine learning workflow — from exploratory data analysis, data cleaning, feature engineering, and model training/tuning, to building a production-ready inference API using FastAPI, containerizing it with Docker, and preparing the service for cloud deployment.

## **📊 Project Overview**

The goal of this project is to classify whether an online browsing session will result in a purchase (`revenue = 1`), making this a binary classification problem.
The dataset contains a mix of:

- Categorical features such as `month`, `visitor_type`, `region`, and `traffic_type` and more.

- Numerical features such as `page_values`, `bounce_rates`, `exit_rates`, and various page-duration metrics.

Three machine learning models were trained and evaluated:

- Logistic Regression

- Random Forest

- XGBoost (selected model)

After comparing performance across ROC AUC, Precision, Recall, and F1-score, XGBoost consistently delivered the strongest balance across metrics.
This model was therefore chosen for deployment, wrapped in a FastAPI inference endpoint and packaged in a Docker container for cloud-ready deployment.

## **🧠 Key EDA Insights**

- Class imbalance: Only ~15% of sessions convert (`revenue = 1`), so the positive class is strongly underrepresented.

- Engagement drives conversion: Higher values for `page_values` and `product_related` (both count and duration) are strongly associated with purchases.

- Bounce & exit behavior: Sessions with high `bounce_rates` and `exit_rates` are very unlikely to convert.

- Visitor type: Surprisingly, `new_visitors` tend to convert more than `returning_visitors` in this dataset.

- Seasonality: Strong seasonal effects, with a pronounced peak in November, likely related to seasonal promotions and events.

- Key categorical features: `month` and `traffic_type` are among the most predictive categorical variables.

- Handling rare categories: Rare categories were grouped into "other" to stabilize estimates and reduce noise from underrepresented levels.

These insights guided feature engineering decisions and model selection.

## **📈 Model Performance Summary**

| Model               | ROC AUC   | Precision | Recall    | F1 Score  |
| ------------------- | --------- | --------- | --------- | --------- |
| Logistic Regression | 0.910     | 0.707     | 0.365     | 0.481     |
| Random Forest       | 0.935     | 0.811     | 0.476     | 0.600     |
| **XGBoost (Final)** | **0.938** | **0.718** | **0.595** | **0.651** |

#### Why XGBoost was selected?

- Best ROC AUC across all models

- Strong recall, important for capturing as many potential buyers as possible

- Highest F1-score, providing a good balance between precision and recall

- Robust to class imbalance and capable of modeling nonlinear relationships

- Most consistent performance across validation folds and confusion matrix metrics
## **🚀 Local Deployment**

This section explains exactly how to run the project locally and in Docker, starting from cloning the repository.

```bash
  git clone https://github.com/tmsnobrega/online_shopper_intention.git
  cd online_shopper_intention
```

This project uses uv for dependency management. To install all required packages exactly as locked in uv.lock, run:
```bash
uv sync
```

Start FastAPI using uvicorn
```bash
uvicorn src.app:app --reload
```

Open the API in your browser (Swagger UI)
```bash
http://localhost:8000/docs
```

Before proceeding, Windows users must install Docker Desktop.
Ensure "Use WSL 2 backend" is enabled.

After installation, ensure Docker is running:
```bash
docker --version
```

Run the following from the repository root (where the Dockerfile is located):
```bash
docker build -t shopper-intent .
```

Run the Docker Container
```bash
docker run -p 8000:8000 shopper-intent
```


## Example prediction using predict.py

This script sends a POST request to the running FastAPI service.

```javascript
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

response = requests.post(url, json=sample)
print(response.json())
```

Run it with:
```bash
python src/predict.py
```

The default model is XGBoost, but it is possible to change the model selected by replacing the `MODEL_PATH` variable in src/model.py
## **☁️ Cloud Deployment (Docker → Render)**

The final XGBoost model is deployed as a FastAPI service running inside a Docker container and hosted on Render, a cloud platform that supports containerized applications.

**1. The project includes a production-ready Dockerfile. This image contains:**

- Python 3.13

- FastAPI + Uvicorn

- All dependencies (installed via uv and uv.lock)

- The trained XGBoost model and DictVectorizer

- The FastAPI app exposed on port 8000

**2. Push Project to GitHub**

- Render automatically pulls your GitHub repository.

**3. Deploy on Render**

On the Render dashboard:

- New → Web Service

- Select your GitHub repo

- Choose Docker as the runtime

Use:

- Dockerfile path: `./Dockerfile`

- Port: `8000`

- Start Command:
```bash
uv run uvicorn src.app:app --host 0.0.0.0 --port 8000
```

Render builds the Docker image, starts the FastAPI service, and provides a public URL.

**4. Access the Live API**

The deployed service is available at:

👉 [https://online-shopper-intention-fastapi.onrender.com/docs](https://online-shopper-intention-fastapi.onrender.com/docs)

This endpoint exposes:

- Interactive Swagger UI

- Live prediction endpoint (POST/predict)

- Full OpenAPI schema

You can send JSON payloads directly through the browser or via API clients. 

## Example prediction using cloud_predict.py
```javascript
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
```

Run it with:
```bash
python src/cloud_predict.py
```
