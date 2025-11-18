from fastapi import FastAPI
from src.model import load_model, predict_single

app = FastAPI()

dv, model = load_model()

@app.post("/predict")
def predict(payload: dict):
    probability = predict_single(payload, dv, model)
    return {"purchase_probability": probability}
