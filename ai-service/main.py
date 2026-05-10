import json

from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from decision_engine import calculate_rule_score, hybrid_decision
from model_service import AnomalyModelService

app = FastAPI(
    title="Hybrid AI Anomaly Detection Service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_service = AnomalyModelService()


class DetectionRequest(BaseModel):
    amount: float = Field(..., example=15000)
    status: str = Field(..., example="FAILED")
    error_count: int = Field(default=0, example=3)
    request_count: int = Field(default=1, example=50)
    response_time_ms: float = Field(default=100, example=800)


class DetectionResponse(BaseModel):
    anomaly: bool
    score: float
    severity: str
    anomaly_type: str
    model_score: float
    rule_score: float
    model_prediction: str


@app.get("/")
def home():
    return {"message": "AI Service Running "}


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "ai-anomaly-detection-service"
    }


@app.post("/detect", response_model=DetectionResponse)
def detect(request: DetectionRequest):
    status_code = 1 if request.status.upper() == "SUCCESS" else 0

    model_input = {
        "amount": request.amount,
        "status_code": status_code,
        "error_count": request.error_count,
        "request_count": request.request_count,
        "response_time_ms": request.response_time_ms
    }

    model_prediction, model_score = model_service.predict(model_input)

    rule_score, anomaly_type, severity = calculate_rule_score(
        amount=request.amount,
        status_code=status_code,
        error_count=request.error_count,
        request_count=request.request_count,
        response_time_ms=request.response_time_ms
    )

    final_score = round((model_score * 0.6) + (rule_score * 0.4), 3)

    anomaly = hybrid_decision(
        model_prediction=model_prediction,
        model_score=model_score,
        rule_score=rule_score
    )

    if not anomaly:
        severity = "LOW"
        anomaly_type = "normal_behavior"

    return DetectionResponse(
        anomaly=anomaly,
        score=final_score,
        severity=severity,
        anomaly_type=anomaly_type,
        model_score=round(model_score, 3),
        rule_score=round(rule_score, 3),
        model_prediction="ANOMALY" if model_prediction == -1 else "NORMAL"
    )


@app.get("/metrics")
def get_metrics():
    with open("model_metrics.json") as f:
        return json.load(f)
