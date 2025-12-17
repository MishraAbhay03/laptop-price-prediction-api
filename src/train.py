import joblib
import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

from utils import load_data, clean_columns


DATA_PATH = "../data/processed/laptop_price.csv"
MODEL_PATH = "../model/laptop_price_model.pkl"
FEATURE_PATH = "../model/feature_columns.json"


def main():
    df = load_data(DATA_PATH)
    df = clean_columns(df)

    TARGET_COL = "price(rupee)"

    X = df.drop(TARGET_COL, axis=1)
    y = df[TARGET_COL]

    # Save raw feature columns (VERY IMPORTANT)
    with open(FEATURE_PATH, "w") as f:
        json.dump(list(X.columns), f)

    categorical_cols = X.select_dtypes(include="object").columns.tolist()
    numerical_cols = X.select_dtypes(exclude="object").columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numerical_cols)
        ]
    )

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("R2 Score:", r2_score(y_test, preds))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))

    joblib.dump(model, MODEL_PATH)
    print("✅ Model saved successfully!")


if __name__ == "__main__":
    main()
