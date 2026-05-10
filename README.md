# AI-Based Anomaly Detection Backend System

<div align="center">

![Java](https://img.shields.io/badge/Java-17-orange?style=for-the-badge&logo=openjdk)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-Microservices-brightgreen?style=for-the-badge&logo=springboot)
![Python](https://img.shields.io/badge/Python-AI_Service-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-ML_API-teal?style=for-the-badge&logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![Status](https://img.shields.io/badge/Status-Research_Project-success?style=for-the-badge)

</div>

---

## 📌 Project Overview

The **AI-Based Anomaly Detection Backend System** is a microservices-based backend platform designed to detect abnormal behaviours, failures, and suspicious patterns in distributed web applications.

This backend system is developed as part of the MSc research project:

> **AI-Based Anomaly Detection System for Microservices-Based Web Applications**

The system contains multiple backend services responsible for user management, order processing, payment handling, API routing, dataset generation, model training, and AI-based anomaly detection.

---

## 🏗️ Backend Architecture

```text
┌──────────────────────────────┐
│        Frontend System       │
│      React + Vite UI         │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│        Gateway Service       │
│     API Routing Layer        │
└───────────────┬──────────────┘
                │
   ┌────────────┼────────────┐
   ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌──────────┐
│  User   │  │  Order  │  │ Payment  │
│ Service │  │ Service │  │ Service  │
└────┬────┘  └────┬────┘  └────┬─────┘
     │            │            │
     ▼            ▼            ▼
┌──────────────────────────────┐
│        Database Layer        │
│          MySQL DB            │
└──────────────────────────────┘
                ▲
                │
                ▼
┌──────────────────────────────┐
│          AI Service          │
│ Dataset Management + Model   │
│ Training + Anomaly Detection │
└──────────────────────────────┘
```

---

## 🧩 Microservices Included

| Service | Description |
|---|---|
| 🌐 Gateway Service | Central API entry point and request routing layer |
| 👤 User Service | Handles user registration, user data, and user-related operations |
| 🛒 Order Service | Manages customer orders and order lifecycle |
| 💳 Payment Service | Handles payment records, simulated failures, and anomaly-triggering events |
| 🤖 AI Service | Handles dataset management, model training, and anomaly detection |

---

## 🌐 Gateway Service

The **Gateway Service** acts as the main entry point for all client requests.

### Responsibilities

- Route API requests to internal services
- Provide unified backend access
- Hide internal microservice details from frontend
- Support future security integration
- Centralized API management

### Example Routes

```text
/api/users/**      → User Service
/api/orders/**     → Order Service
/api/payments/**   → Payment Service
/api/ai/**         → AI Service
```

---

## 👤 User Service

The **User Service** manages user-related backend operations.

### Responsibilities

- Create users
- Update user details
- Retrieve user information
- Delete users
- Provide user data for order and payment flows

### Main Functional Areas

```text
User Registration
User Profile Management
User Lookup
User CRUD Operations
```

---

## 🛒 Order Service

The **Order Service** manages order-related business logic.

### Responsibilities

- Create new orders
- Retrieve order details
- Update order status
- Track order lifecycle
- Connect order data with payment processing

### Example Order States

```text
CREATED
PROCESSING
COMPLETED
FAILED
CANCELLED
```

---

## 💳 Payment Service

The **Payment Service** is one of the core services in the anomaly detection workflow.

It handles payment operations and generates behavioural data that can be analyzed by the AI service.

### Responsibilities

- Create payment records
- Process payment requests
- Simulate successful and failed payments
- Generate abnormal payment patterns
- Send detection requests to AI Service
- Store anomaly-related payment information

### Payment Data Example

```json
{
  "orderId": 1001,
  "amount": 25000.00,
  "status": "FAILED",
  "responseTimeMs": 3500,
  "errorCount": 4,
  "requestCount": 12,
  "anomaly": true,
  "anomalyType": "HIGH_AMOUNT_FAILURE",
  "severity": "HIGH"
}
```

---

## 🤖 AI Service

The **AI Service** is responsible for intelligent anomaly detection.

This service includes:

- Dataset generation
- Dataset management
- Feature extraction
- Model training
- Model evaluation
- Anomaly prediction
- AI detection API endpoints

---

## 🧠 AI Service Functional Scope

### 1. Dataset Management

The AI service manages datasets collected from backend microservices.

Dataset records may include:

```text
amount
status
error_count
request_count
response_time_ms
service_name
timestamp
anomaly_label
anomaly_type
severity
```

---

### 2. Model Training

The AI service supports training machine learning models using collected system behaviour data.

### Training Workflow

```text
Collect Microservice Data
        ↓
Clean Dataset
        ↓
Extract Features
        ↓
Train ML Model
        ↓
Evaluate Model
        ↓
Save Trained Model
        ↓
Use Model for Prediction
```

---

### 3. Anomaly Detection

The AI service exposes prediction endpoints that allow other services to detect whether a request or event is abnormal.

### Example Detection Request

```json
{
  "amount": 50000,
  "status": "FAILED",
  "error_count": 5,
  "request_count": 15,
  "response_time_ms": 4200
}
```

### Example Detection Response

```json
{
  "anomaly": true,
  "anomalyType": "SUSPICIOUS_PAYMENT_BEHAVIOUR",
  "severity": "CRITICAL",
  "confidence": 0.94
}
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Backend Framework | Spring Boot |
| API Gateway | Spring Cloud Gateway |
| AI Service | Python / FastAPI |
| Machine Learning | Scikit-learn / Pandas / NumPy |
| Database | MySQL |
| API Communication | REST APIs |
| Build Tool | Maven |
| Containerization | Docker |
| Testing | Postman / JUnit |
| Architecture | Microservices |

---

## 📂 Project Structure

```bash
anomaly-detection-backend/
│
├── gateway-service/
│   ├── src/
│   ├── pom.xml
│   └── README.md
│
├── user-service/
│   ├── src/
│   ├── pom.xml
│   └── README.md
│
├── order-service/
│   ├── src/
│   ├── pom.xml
│   └── README.md
│
├── payment-service/
│   ├── src/
│   ├── pom.xml
│   └── README.md
│
├── ai-service/
│   ├── app/
│   ├── dataset/
│   ├── models/
│   ├── scripts/
│   ├── requirements.txt
│   └── README.md
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Service Ports

| Service | Port |
|---|---|
| Gateway Service | `8080` |
| User Service | `8081` |
| Order Service | `8082` |
| Payment Service | `8083` |
| AI Service | `5000` |
| MySQL Database | `3306` |

---

## 🚀 Getting Started

### Prerequisites

Make sure the following tools are installed:

```text
Java 17+
Maven
Python 3.10+
Node.js
MySQL
Docker
Postman
```

---

## ▶️ Run Backend Services Manually

### 1. Start Gateway Service

```bash
cd gateway-service
mvn spring-boot:run
```

---

### 2. Start User Service

```bash
cd user-service
mvn spring-boot:run
```

---

### 3. Start Order Service

```bash
cd order-service
mvn spring-boot:run
```

---

### 4. Start Payment Service

```bash
cd payment-service
mvn spring-boot:run
```

---

### 5. Start AI Service

```bash
cd ai-service
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 5000
```

---

## 🐳 Run With Docker Compose

```bash
docker-compose up --build
```

Stop services:

```bash
docker-compose down
```

---

## 🌐 API Endpoint Summary

### Gateway

```text
GET  /api/health
```

### User Service

```text
GET     /api/users
GET     /api/users/{id}
POST    /api/users
PUT     /api/users/{id}
DELETE  /api/users/{id}
```

### Order Service

```text
GET     /api/orders
GET     /api/orders/{id}
POST    /api/orders
PUT     /api/orders/{id}
DELETE  /api/orders/{id}
```

### Payment Service

```text
GET     /api/payments
GET     /api/payments/{id}
POST    /api/payments
PUT     /api/payments/{id}
DELETE  /api/payments/{id}
POST    /api/payments/detect
```

### AI Service

```text
GET     /health
POST    /detect
POST    /train
GET     /dataset
POST    /dataset/generate
GET     /model/status
```

---

## 🔄 Backend Data Flow

```text
Frontend sends request
        ↓
Gateway Service receives request
        ↓
Request forwarded to target microservice
        ↓
Microservice processes business logic
        ↓
Payment Service sends behaviour data to AI Service
        ↓
AI Service predicts anomaly
        ↓
Prediction result saved with transaction
        ↓
Frontend displays anomaly result
```

---

## 🧪 Model Training Flow

```text
Payment / Order / User Activity Data
        ↓
Dataset Generator
        ↓
Preprocessing
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Persistence
        ↓
Prediction API
```

---

## 🧬 AI Features Used

| Feature | Meaning |
|---|---|
| `amount` | Payment amount |
| `status` | Payment status |
| `error_count` | Number of errors |
| `request_count` | Number of requests |
| `response_time_ms` | Response time |
| `service_name` | Source microservice |
| `anomaly_label` | Normal or abnormal classification |

---

## 📊 Anomaly Severity Levels

| Severity | Description |
|---|---|
| LOW | Minor unusual behaviour |
| MEDIUM | Suspicious system behaviour |
| HIGH | Strong anomaly indicator |
| CRITICAL | Severe abnormal activity |

---

## 🔐 Security Considerations

Future security improvements may include:

- JWT authentication
- Role-based access control
- API Gateway security filters
- Rate limiting
- Service-to-service authentication
- Secure environment variables
- Audit logging

---

## 📦 Environment Variables

Example `.env` values:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=anomaly_db
MYSQL_USERNAME=root
MYSQL_PASSWORD=root

AI_SERVICE_URL=http://localhost:5000
GATEWAY_PORT=8080
USER_SERVICE_PORT=8081
ORDER_SERVICE_PORT=8082
PAYMENT_SERVICE_PORT=8083
```

---

### Test APIs Using Postman

Import backend endpoints into Postman and test:

```text
User CRUD
Order CRUD
Payment CRUD
AI Detection
Dataset Generation
Model Training
```

---

## 📈 Future Enhancements

- Service discovery using Eureka or Consul
- Centralized logging using ELK Stack
- Distributed tracing using Zipkin or Jaeger
- Kafka-based event streaming
- Kubernetes deployment
- Prometheus and Grafana monitoring
- Advanced deep learning models
- LSTM-based anomaly detection
- Real-time WebSocket alerts
- Automated dataset versioning
- Model retraining pipeline

---

## 🎓 Academic Research Context

This backend system supports the MSc research project:

> **AI-Based Anomaly Detection System for Microservices-Based Web Applications**

The backend demonstrates how AI can be integrated into real-world distributed systems to detect failures, abnormal behaviours, suspicious transactions, and system performance anomalies.

---

## 👨‍💻 Author

<div align="center">

## **Sahan Nimesha**

Software Engineer | Full Stack Developer | AI Researcher

</div>

---

## 📄 Copyright

```text
© 2026 Sahan Nimesha. All Rights Reserved.
```

This backend system, including source code, architecture, AI service design, dataset management workflow, documentation, and implementation concepts, is the intellectual property of **Sahan Nimesha**.

Unauthorized copying, modification, distribution, commercial usage, or academic misuse without written permission is strictly prohibited.

---

## ⭐ Final Note

<div align="center">

### Built by **Sahan Nimesha**

### Intelligent Systems. Scalable Architecture. Real-Time Detection.

</div>