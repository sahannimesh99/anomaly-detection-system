def calculate_rule_score(
        amount: float,
        status_code: int,
        error_count: int,
        request_count: int,
        response_time_ms: float
) -> tuple[float, str, str]:
    score = 0.0
    anomaly_type = "NORMAL_BEHAVIOR"
    severity = "LOW"

    if amount > 10000:
        score += 0.25
        anomaly_type = "HIGH_VALUE_TRANSACTION"

    if status_code == 0:
        score += 0.25
        anomaly_type = "PAYMENT_FAILURE"

    if error_count >= 3:
        score += 0.20
        anomaly_type = "ERROR_SPIKE"

    if response_time_ms > 700:
        score += 0.20
        anomaly_type = "LATENCY_SPIKE"

    if request_count > 70:
        score += 0.10
        anomaly_type = "TRAFFIC_SPIKE"

    if score >= 0.75:
        severity = "CRITICAL"
    elif score >= 0.50:
        severity = "HIGH"
    elif score >= 0.25:
        severity = "MEDIUM"

    return min(score, 1.0), anomaly_type, severity


def hybrid_decision(model_prediction: int, model_score: float, rule_score: float) -> bool:
    # IsolationForest returns -1 for anomaly, 1 for normal.
    model_detected = model_prediction == -1

    return model_detected or rule_score >= 0.25 or model_score >= 0.65