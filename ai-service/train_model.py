import json
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
METRICS_PATH = os.path.join(BASE_DIR, "model_metrics.json")

RF_MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.pkl")
ANOMALY_MODEL_PATH = os.path.join(MODEL_DIR, "anomaly_model.pkl")
ISO_MODEL_PATH = os.path.join(MODEL_DIR, "iso_model.pkl")

FEATURES = [
    "amount",
    "status_code",
    "error_count",
    "request_count",
    "response_time_ms",
    "transactions_last_1min",
    "avg_amount_last_5min",
    "failure_rate",
    "hour_of_day"
]

TARGET = "is_anomaly"


def train_models():
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(DATASET_PATH):
        print(" Dataset missing. Generating new dataset first...")
        from generate_dataset import run_dataset_generation
        run_dataset_generation()

    # LOAD DATASET
    df = pd.read_csv(DATASET_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    print("\n===== DATASET INFO =====")
    print(f"Total Records: {len(df)}")
    print(f"Features Used: {len(FEATURES)}")

    # TRAIN / TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # RANDOM FOREST MODEL
    rf_model = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ))
    ])

    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_report = classification_report(y_test, rf_pred, output_dict=True)

    joblib.dump(rf_model, RF_MODEL_PATH)
    joblib.dump(rf_model, ANOMALY_MODEL_PATH)

    # ISOLATION FOREST MODEL
    iso_model = Pipeline([
        ("scaler", StandardScaler()),
        ("iso", IsolationForest(
            contamination=0.3,
            random_state=42
        ))
    ])

    iso_model.fit(X_train)
    iso_pred_raw = iso_model.predict(X_test)
    iso_pred = [1 if x == -1 else 0 for x in iso_pred_raw]
    iso_report = classification_report(y_test, iso_pred, output_dict=True)

    joblib.dump(iso_model, ISO_MODEL_PATH)

    rf_p = round(rf_report["weighted avg"]["precision"], 3)
    rf_r = round(rf_report["weighted avg"]["recall"], 3)
    rf_f1 = round(rf_report["weighted avg"]["f1-score"], 3)

    iso_p = round(iso_report["weighted avg"]["precision"], 3)
    iso_r = round(iso_report["weighted avg"]["recall"], 3)
    iso_f1 = round(iso_report["weighted avg"]["f1-score"], 3)

    metrics = {
        "random_forest": {
            "precision": rf_p,
            "recall": rf_r,
            "f1": rf_f1,
            "f1_score": rf_f1
        },
        "isolation_forest": {
            "precision": iso_p,
            "recall": iso_r,
            "f1": iso_f1,
            "f1_score": iso_f1
        }
    }

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    print("\n Both models trained and saved successfully.")
    return metrics


if __name__ == "__main__":
    train_models()