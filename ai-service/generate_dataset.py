import requests
import pandas as pd
from datetime import datetime

API_URL = "http://localhost:8083/payments"

def fetch_data():
    response = requests.get(f"{API_URL}?size=10000")
    response.raise_for_status()
    data = response.json()
    return data.get("content", [])

def transform(data):
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

            #  NEW FEATURES
            "transactions_last_1min": total_transactions,
            "avg_amount_last_5min": avg_amount,
            "failure_rate": failure_rate,
            "hour_of_day": current_hour,

            "is_anomaly": 1 if item.get("anomaly") else 0
        }
        rows.append(row)

    return pd.DataFrame(rows)

def save_csv(df):
    df.to_csv("dataset.csv", index=False)
    print(" Advanced dataset saved")

if __name__ == "__main__":
    data = fetch_data()
    df = transform(data)
    save_csv(df)