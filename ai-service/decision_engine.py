def calculate_rule_score(
        amount: float,
        status_code: int,
        error_count: int,
        request_count: int,
        response_time_ms: float
) -> tuple[float, str, str]:
    score = 0.0
    anomaly_type = "normal_behavior"
    severity = "LOW"

    if amount > 10000:
        score += 0.25
        anomaly_type = "high_value_transaction"

    if status_code == 0:
        score += 0.25
        anomaly_type = "payment_failure"

    if error_count >= 3:
        score += 0.20
        anomaly_type = "error_spike"

    if response_time_ms > 700:
        score += 0.20
        anomaly_type = "latency_spike"

    if request_count > 70:
        score += 0.10
        anomaly_type = "traffic_spike"

    if score >= 0.75:
        severity = "CRITICAL"
    elif score >= 0.50:
        severity = "HIGH"
    elif score >= 0.30:
        severity = "MEDIUM"

    return min(score, 1.0), anomaly_type, severity


def hybrid_decision(model_prediction: int, model_score: float, rule_score: float) -> bool:
    # IsolationForest returns -1 for anomaly, 1 for normal.
    model_detected = model_prediction == -1

    return model_detected or rule_score >= 0.50 or model_score >= 0.65