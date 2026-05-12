import os

import joblib
import pandas as pd

MODEL_PATH = os.path.join("models", "anomaly_model.pkl")

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

    def load_model(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError("Model not found. Train first.")

        self.model = joblib.load(MODEL_PATH)
        self.last_loaded_time = os.path.getmtime(MODEL_PATH)
        print(" Model loaded")

    def check_reload(self):
        current_modified_time = os.path.getmtime(MODEL_PATH)

        if current_modified_time != self.last_loaded_time:
            print(" Model updated — reloading...")
            self.load_model()

    def predict(self, data: dict):
        self.check_reload()

        input_df = pd.DataFrame([data], columns=FEATURES)

        prediction = self.model.predict(input_df)[0]

        return prediction

    def predict(self, data: dict):
        self.check_reload()
        input_df = pd.DataFrame([data], columns=FEATURES)

        # prediction
        prediction = self.model.predict(input_df)[0]

        # confidence score
        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(input_df)[0]
            model_score = float(max(probabilities))
            return None

        else:
            # fallback score for models without probabilities
            model_score = 0.8 if prediction == -1 else 0.2

            return prediction, round(model_score, 3)

