# 🛡️ AI-Based Anomaly Detection System (Backend & AI Core)

<div align="center">

![Java](https://img.shields.io/badge/Java-17-orange?style=for-the-badge&logo=openjdk)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.x-brightgreen?style=for-the-badge&logo=springboot)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-1.3+-orange?style=for-the-badge&logo=scikitlearn)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue?style=for-the-badge&logo=mysql)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![Status](https://img.shields.io/badge/Status-Complete_&_Verified-success?style=for-the-badge)

</div>

---

## 📌 Submission Checklist & Artifact Mapping

This repository forms the complete backend, database, microservices, and AI machine learning core for the research project: **"AI-Based Anomaly Detection System for Microservices-Based Web Applications"**.

Below is the audit matrix mapping project components to submission requirements:

| Submission Requirement | Location / File Path | Description |
|---|---|---|
| **Complete Source Code** | `gateway-service/`, `user-service/`, `order-service/`, `payment-service/`, `ai-service/` | Full source code for all 5 microservices. |
| **Model Training & Evaluation Scripts** | `ai-service/train_model.py` | Trains Random Forest & Isolation Forest pipelines; evaluates precision, recall, & F1 score. |
| **Data Preprocessing & Feature Engineering** | `ai-service/generate_dataset.py`, `ai-service/decision_engine.py` | Extracts 9 feature dimensions, transforms telemetry data, and scales features via StandardScaler. |
| **Front-end Component** | [`d:/anomaly-detection-system-portal`](file:///d:/anomaly-detection-system-portal) | React 19 + Vite dashboard portal with real-time charts, Dark/Light mode, and CRUD management. |
| **Back-end Component** | `gateway-service/`, `user-service/`, `order-service/`, `payment-service/` | Spring Boot 3 Java microservices with RESTful APIs. |
| **AI Detection Service** | `ai-service/main.py`, `ai-service/model_service.py` | FastAPI server managing real-time detection requests, model persistence, and automated retraining. |
| **Database Components & Schemas** | `init-db.sql` | MySQL schema initialization scripts for `user_db`, `order_db`, and `payment_db`. |
| **Configuration Files** | `docker-compose.yml`, `*/src/main/resources/application.yml` | Central Docker deployment config and microservice application properties. |
| **Dependency & Package Files** | `pom.xml`, `ai-service/requirements.txt`, `package.json` | Maven dependencies for Java, PyPI packages for Python AI, and npm dependencies for React UI. |
| **Test Evidence** | `walkthrough.md`, `ai-service/model_metrics.json` | Evaluation logs, automated test results, and browser execution recordings. |
| **Trained Model Files** | `ai-service/models/rf_model.pkl`, `iso_model.pkl`, `anomaly_model.pkl` | Serialized scikit-learn models ready for real-time inference. |
| **Sample Dataset & Instructions** | `ai-service/dataset.csv` | Pre-generated 9-feature payment anomaly telemetry dataset. |
| **Deployment Configuration** | `docker-compose.yml`, `Dockerfile` in each service | One-click multi-container orchestration. |

---

## 🏗️ Architecture & Component Overview

```text
┌─────────────────────────────────────────────────────────┐
│              Frontend Application Portal                │
│         React 19 + Vite UI (Port 5173 / 80)             │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│               Spring Cloud API Gateway                  │
│                     (Port 8080)                         │
└──────┬─────────────────────┼─────────────────────┬──────┘
       │                     │                     │
       ▼                     ▼                     ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ User Service │      │ Order Service│      │PaymentService│
│ (Port 8081)  │      │ (Port 8082)  │      │ (Port 8083)  │
└──────┬───────┘      └──────┬───────┘      └──────┬───────┘
       │                     │                     │
       ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────┐
│                 MySQL Relational DB                     │
│    databases: user_db | order_db | payment_db           │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│           FastAPI Hybrid AI Detection Engine            │
│               Python Service (Port 5000)                │
│   Random Forest Classifier + Isolation Forest Model     │
└─────────────────────────────────────────────────────────┘
```

---

## 💻 System Requirements

### Software Requirements
- **Java Development Kit (JDK)**: Java 17 or higher
- **Build Tool**: Apache Maven 3.8+
- **Python**: Python 3.10 or higher
- **Node.js**: Node.js 18.x or 20.x
- **Database**: MySQL 8.0+
- **Containerization**: Docker Desktop 4.x+ & Docker Compose v2+
- **Browser**: Google Chrome, Microsoft Edge, or Firefox (for UI portal)

### Hardware Requirements
- **Processor**: Intel Core i5 / AMD Ryzen 5 or Apple Silicon (M1/M2/M3)
- **Memory (RAM)**: 8 GB RAM minimum (16 GB recommended for running full Docker stack)
- **Disk Space**: 5 GB available disk space

---

## 🛠️ Languages, Libraries, and Frameworks Used

| Layer | Technology / Library | Usage |
|---|---|---|
| **Backend Framework** | Java 17, Spring Boot 3.x, Spring Data JPA | Business logic for User, Order, and Payment services |
| **API Gateway** | Spring Cloud Gateway | Centralized routing, CORS deduplication, and port mapping |
| **AI Framework** | Python 3.10+, FastAPI, Uvicorn | High-performance async ML inference API server |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, Joblib | Model training (Random Forest & Isolation Forest), dataset handling |
| **Database** | MySQL 8.0, Hibernate ORM | Transaction data persistence |
| **Frontend Portal** | React 19, Vite 8, Chart.js, Lucide/React-Icons | Interactive web UI, real-time analytics & theme control |
| **Build & Tooling** | Maven, npm, Docker Compose | Dependency management and container orchestration |

---

## ⚙️ Service Ports & Environment Configurations

| Service | Port | Base Path | Role |
|---|---|---|---|
| **API Gateway** | `8080` | `http://localhost:8080/api` | Central API Entry Point |
| **User Service** | `8081` | `http://localhost:8081` | User Management CRUD |
| **Order Service** | `8082` | `http://localhost:8082` | Order Processing |
| **Payment Service** | `8083` | `http://localhost:8083` | Transaction Processing & Anomaly Triggers |
| **AI Service** | `5000` | `http://localhost:5000` | Machine Learning Inference & Pipeline Refresh |
| **MySQL DB** | `3306` | `localhost:3306` | Relational Database |
| **Frontend Portal** | `5173` | `http://localhost:5173` | React User Interface |

### Default Credentials
- **Database User**: `root`
- **Database Password**: `root`
- **Database Names**: `user_db`, `order_db`, `payment_db`

---

## 🚀 Installation & Setup Procedure

### Option A: Running with Docker Compose (Recommended One-Click Method)

1. Clone the repository and navigate to the project root:
   ```bash
   cd anomaly-detection-system
   ```

2. Start all backend microservices, database, and AI service:
   ```bash
   docker-compose up --build
   ```

3. To stop all services:
   ```bash
   docker-compose down
   ```

---

### Option B: Manual Local Setup (Step-by-Step)

#### Step 1: Database Setup
1. Ensure MySQL is running on `localhost:3306`.
2. Execute the initialization script `init-db.sql`:
   ```bash
   mysql -u root -p < init-db.sql
   ```

#### Step 2: Build & Start Spring Boot Microservices
Open separate terminal windows for each service:

1. **User Service**:
   ```bash
   cd user-service
   mvn clean install
   mvn spring-boot:run
   ```
2. **Order Service**:
   ```bash
   cd order-service
   mvn clean install
   mvn spring-boot:run
   ```
3. **Payment Service**:
   ```bash
   cd payment-service
   mvn clean install
   mvn spring-boot:run
   ```
4. **API Gateway**:
   ```bash
   cd api-gateway
   mvn clean install
   mvn spring-boot:run
   ```

#### Step 3: Set Up & Start Python AI Service
1. Navigate to `ai-service`:
   ```bash
   cd ai-service
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   py -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run dataset generation and model training (or let the service do it automatically):
   ```bash
   py generate_dataset.py
   py train_model.py
   ```
5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 5000
   ```

#### Step 4: Start Frontend Portal
Navigate to the frontend workspace (`anomaly-detection-system-portal`):
```bash
cd ../anomaly-detection-system-portal
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 🤖 Dataset Preparation & Model Training

### 1. Feature Engineering
The AI system processes 9 distinct telemetry feature dimensions:
- `amount`: Payment transaction value
- `status_code`: Success (`1`) or Failure (`0`)
- `error_count`: Number of accumulated service errors
- `request_count`: Total requests in window
- `response_time_ms`: Latency duration
- `transactions_last_1min`: Velocity metric
- `avg_amount_last_5min`: Moving average transaction value
- `failure_rate`: Ratio of failed transactions
- `hour_of_day`: Temporal feature (`0`-`23`)

### 2. Manual Training Execution
To trigger model training manually via CLI:
```bash
cd ai-service
py generate_dataset.py
py train_model.py
```

### 3. Automated GUI Retraining (One-Click)
The system supports automated dataset generation and model retraining directly from the user interface:
1. Open the portal at `http://localhost:5173`.
2. Click **"⟳ Refresh Data"** or **"⚡ Retrain AI Models"**.
3. The frontend invokes `/pipeline/refresh`, which generates fresh telemetry data, trains both **Random Forest** and **Isolation Forest** models, updates `model_metrics.json`, and reloads the active models in memory without service interruption.

---

## 🌐 API Integration Reference

### Gateway Unified API Endpoints (`http://localhost:8080/api`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/payments?page=0&size=10&filter=all` | Paginated transaction list |
| `POST` | `/api/payments` | Process payment & execute AI anomaly check |
| `GET` | `/api/users` | List all registered users |
| `POST` | `/api/users` | Register a new user |
| `GET` | `/api/orders` | List all orders |
| `POST` | `/api/orders` | Create an order |

### AI Service Endpoints (`http://localhost:5000`)

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/detect` | Hybrid AI anomaly prediction |
| `GET` | `/metrics` | Model precision, recall, and F1 scores |
| `POST` | `/pipeline/refresh` | Auto-generate dataset, train models & reload in memory |
| `GET` | `/health` | Service status check |

---

## ⚠️ Known Limitations & Design Considerations

1. **Self-Contained Fallback Mode**: If Spring Boot backend services or MySQL DB are disconnected, the frontend portal and AI service automatically utilize built-in fallback telemetry generators to maintain continuous UI evaluation without breaking.
2. **Model Persistence**: Serialized model pickles (`.pkl` files) are saved locally under `ai-service/models/`. For production distributed environments, a centralized model registry (such as MLflow) is recommended.
3. **Contamination Parameter**: The Isolation Forest model assumes a default contamination hyperparameter of `0.25`, which can be fine-tuned based on domain-specific anomaly frequencies.

---

## 🔑 External Services & API Keys

- **No External Paid APIs Required**: The system is completely self-contained and operates 100% locally without external third-party subscriptions or cloud API keys.

---

## 📄 License & Academic Attribution

```text
© 2026 Sahan Nimesha. All Rights Reserved.
MSc Research Project: AI-Based Anomaly Detection System for Microservices-Based Web Applications
```