from fastapi import FastAPI
import joblib
import pandas as pd
import json
from pathlib import Path

from schema import LaptopFeatures

app = FastAPI(
    title="Laptop Price Prediction API",
    version="1.0"
)

# Load model
BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "model" / "laptop_price_model.pkl"
features_path = BASE_DIR / "model" / "feature_columns.json"

model = joblib.load(model_path)

with open(features_path, "r") as f:
    feature_columns = json.load(f)



@app.get("/")
def home():
    return {"message": "Laptop Price Prediction API is running"}


@app.post("/predict")
def predict_price(data: LaptopFeatures):

    # Map API fields to model feature names
    input_dict = {
        "company": data.company,
        "product": data.product,
        "typename": data.typename,
        "inches": data.inches,
        "screenresolution": data.screenresolution,
        "cpu_company": data.cpu_company,
        "cpu_type": data.cpu_type,
        "cpu_frequency_(ghz)": data.cpu_frequency_ghz,
        "ram_(gb)": data.ram_gb,
        "memory": data.memory,
        "gpu_company": data.gpu_company,
        "gpu_type": data.gpu_type,
        "opsys": data.opsys,
        "weight_(kg)": data.weight_kg
    }

    df = pd.DataFrame([input_dict])
    df = df[model.feature_names_in_]

    prediction = model.predict(df)

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }
