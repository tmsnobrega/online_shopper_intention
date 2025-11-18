import pickle
import numpy as np


MODEL_PATH = "models/xgboost.pkl"   # select the model


def load_model(model_path: str = MODEL_PATH):
    """
    Loads the DictVectorizer and model from a .pkl file.
    """
    with open(model_path, "rb") as f:
        artifacts = pickle.load(f)

    dv = artifacts["dv"]
    model = artifacts["model"]

    return dv, model


def predict_single(sample: dict, dv, model) -> float:
    """
    Receives one JSON dictionary, applies DictVectorizer, 
    and returns the model's probability prediction.
    """
    X = dv.transform([sample])  # list of one dictionary
    y_pred = model.predict_proba(X)[0, 1]
    return float(y_pred)
