import json
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DATASET_PATH = "dataset.csv"
MODEL_DIR = "models"

RF_MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.pkl")
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

    print(f"Training Records: {len(X_train)}")
    print(f"Testing Records: {len(X_test)}")

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

    rf_report = classification_report(
        y_test,
        rf_pred,
        output_dict=True
    )

    print("\n===== Random Forest Evaluation =====")
    print(classification_report(y_test, rf_pred))

    joblib.dump(rf_model, RF_MODEL_PATH)


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

    # Convert predictions
    # -1 = anomaly → 1
    #  1 = normal  → 0

    iso_pred = [1 if x == -1 else 0 for x in iso_pred_raw]

    iso_report = classification_report(
        y_test,
        iso_pred,
        output_dict=True
    )

    print("\n===== Isolation Forest Evaluation =====")
    print(classification_report(y_test, iso_pred))

    joblib.dump(iso_model, ISO_MODEL_PATH)

    metrics = {
        "random_forest": {
            "precision": round(
                rf_report["weighted avg"]["precision"], 3
            ),
            "recall": round(
                rf_report["weighted avg"]["recall"], 3
            ),
            "f1_score": round(
                rf_report["weighted avg"]["f1-score"], 3
            )
        },
        "isolation_forest": {
            "precision": round(
                iso_report["weighted avg"]["precision"], 3
            ),
            "recall": round(
                iso_report["weighted avg"]["recall"], 3
            ),
            "f1_score": round(
                iso_report["weighted avg"]["f1-score"], 3
            )
        }
    }

    with open("model_metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("\n===== METRICS SAVED =====")
    print(json.dumps(metrics, indent=4))

    print("\n Both models trained and saved successfully.")


if __name__ == "__main__":
    train_models()