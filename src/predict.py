import joblib
import pandas as pd

MODEL_PATH = "../model/laptop_price_model.pkl"

def predict(sample: dict):
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([sample])
    prediction = model.predict(df)
    return float(prediction[0])


if __name__ == "__main__":
    example = {
        "ram": 8,
        "weight": 1.8,
        "company": "Dell",
        "type_name": "Ultrabook",
        "cpu_brand": "Intel",
        "gpu_brand": "Intel",
        "os": "Windows 10"
    }

    print("Predicted Price:", predict(example))
