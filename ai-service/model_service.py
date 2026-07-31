import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "models", "anomaly_model.pkl")
RF_MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.pkl")

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


class AnomalyModelService:

    def __init__(self):
        self.model = None
        self.last_loaded_time = 0
        self.load_model()

    def get_active_model_path(self):
        if os.path.exists(MODEL_PATH):
            return MODEL_PATH
        if os.path.exists(RF_MODEL_PATH):
            return RF_MODEL_PATH
        return None

    def load_model(self):
        target_path = self.get_active_model_path()
        if not target_path or not os.path.exists(target_path):
            print(" Model not found yet. Will train on demand.")
            self.model = None
            return

        self.model = joblib.load(target_path)
        self.last_loaded_time = os.path.getmtime(target_path)
        print(" AI Model loaded into memory successfully.")

    def check_reload(self):
        target_path = self.get_active_model_path()
        if not target_path or not os.path.exists(target_path):
            return

        current_modified_time = os.path.getmtime(target_path)
        if current_modified_time != self.last_loaded_time or self.model is None:
            print(" Model updated — reloading into service...")
            self.load_model()

    def predict(self, data: dict):
        self.check_reload()

        if self.model is None:
            # Fallback prediction if model pickle hasn't been created
            is_high_amount = data.get("amount", 0) > 5000
            is_failed = data.get("status_code", 1) == 0
            prediction = -1 if (is_high_amount or is_failed) else 1
            model_score = 0.85 if prediction == -1 else 0.15
            return prediction, model_score

        # Prepare feature dict
        input_data = {
            "amount": data.get("amount", 0),
            "status_code": data.get("status_code", 1),
            "error_count": data.get("error_count", 0),
            "request_count": data.get("request_count", 1),
            "response_time_ms": data.get("response_time_ms", 120),
            "transactions_last_1min": data.get("transactions_last_1min", 10),
            "avg_amount_last_5min": data.get("avg_amount_last_5min", 250.0),
            "failure_rate": data.get("failure_rate", 0.05),
            "hour_of_day": data.get("hour_of_day", 12)
        }

        input_df = pd.DataFrame([input_data], columns=FEATURES)

        prediction = self.model.predict(input_df)[0]

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(input_df)[0]
            model_score = float(max(probabilities))
        else:
            model_score = 0.85 if prediction == -1 else 0.15

        return prediction, round(model_score, 3)
