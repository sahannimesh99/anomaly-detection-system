import requests
import pandas as pd
from datetime import datetime
import random
import os

API_URL = "http://localhost:8083/payments"
DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")

def fetch_data():
    response = requests.get(f"{API_URL}?size=10000", timeout=3)
    response.raise_for_status()
    data = response.json()
    return data.get("content", [])

def generate_synthetic_data(num_samples=200):
    rows = []
    current_hour = datetime.now().hour
    for i in range(num_samples):
        is_anomaly = random.random() < 0.25
        amount = random.uniform(5000, 25000) if is_anomaly else random.uniform(10, 800)
        status_code = 0 if (is_anomaly and random.random() < 0.6) else 1
        rows.append({
            "amount": round(amount, 2),
            "status_code": status_code,
            "error_count": 3 if status_code == 0 else 0,
            "request_count": num_samples,
            "response_time_ms": 800 if status_code == 0 else 120,
            "transactions_last_1min": num_samples,
            "avg_amount_last_5min": 250.0,
            "failure_rate": 0.25 if is_anomaly else 0.05,
            "hour_of_day": current_hour,
            "is_anomaly": 1 if is_anomaly else 0
        })
    return pd.DataFrame(rows)

def transform(data):
    if not data:
        return generate_synthetic_data()

    rows = []
    total_transactions = len(data)
    failed_count = sum(1 for x in data if x.get("status") == "FAILED")
    avg_amount = sum(x.get("amount", 0) for x in data) / max(total_transactions, 1)
    failure_rate = failed_count / max(total_transactions, 1)
    current_hour = datetime.now().hour

    for item in data:
        row = {
            "amount": item.get("amount", 0),
            "status_code": 1 if item.get("status") == "SUCCESS" else 0,
            "error_count": 3 if item.get("status") == "FAILED" else 0,
            "request_count": total_transactions,
            "response_time_ms": 800 if item.get("status") == "FAILED" else 120,

            # FEATURES
            "transactions_last_1min": total_transactions,
            "avg_amount_last_5min": avg_amount,
            "failure_rate": failure_rate,
            "hour_of_day": current_hour,

            "is_anomaly": 1 if item.get("anomaly") else 0
        }
        rows.append(row)

    return pd.DataFrame(rows)

def save_csv(df):
    df.to_csv(DATASET_PATH, index=False)
    print(f" Dataset saved to {DATASET_PATH} with {len(df)} records")

def run_dataset_generation():
    try:
        data = fetch_data()
        df = transform(data)
    except Exception as e:
        print(f" Live fetch error: {e}. Generating dataset...")
        df = generate_synthetic_data()
    save_csv(df)
    return len(df)

if __name__ == "__main__":
    run_dataset_generation()