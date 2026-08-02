-- =========================================================
-- Anomaly Detection System - Complete Database Schemas & Seed Data
-- =========================================================

CREATE DATABASE IF NOT EXISTS user_db;
CREATE DATABASE IF NOT EXISTS order_db;
CREATE DATABASE IF NOT EXISTS payment_db;

-- ---------------------------------------------------------
-- 1. USER DATABASE SCHEMA & SEED DATA
-- ---------------------------------------------------------
USE user_db;

CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (id, name, email) VALUES
(1, 'Alice Johnson', 'alice.j@example.com'),
(2, 'Bob Smith', 'bob.smith@example.com'),
(3, 'Charlie Davis', 'charlie.d@example.com'),
(4, 'Diana Prince', 'diana.p@example.com'),
(5, 'Evan Wright', 'evan.w@example.com')
ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email);

-- ---------------------------------------------------------
-- 2. ORDER DATABASE SCHEMA & SEED DATA
-- ---------------------------------------------------------
USE order_db;

CREATE TABLE IF NOT EXISTS orders (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    product VARCHAR(255) NOT NULL,
    amount DOUBLE NOT NULL,
    anomaly BOOLEAN DEFAULT FALSE,
    anomaly_type VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (id, user_id, product, amount, anomaly, anomaly_type) VALUES
(501, 1, 'MacBook Pro M3', 2499.99, FALSE, NULL),
(502, 2, 'Enterprise Server Rack', 12500.00, TRUE, 'Unusual High Amount'),
(503, 3, 'Wireless Mouse', 89.50, FALSE, NULL),
(504, 4, '4K Gaming Monitor', 4999.00, TRUE, 'Rapid Velocity'),
(505, 5, 'USB-C Adapter', 34.00, FALSE, NULL)
ON DUPLICATE KEY UPDATE product=VALUES(product), amount=VALUES(amount), anomaly=VALUES(anomaly);

-- ---------------------------------------------------------
-- 3. PAYMENT DATABASE SCHEMA & SEED DATA
-- ---------------------------------------------------------
USE payment_db;

CREATE TABLE IF NOT EXISTS payments (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT NOT NULL,
    amount DOUBLE NOT NULL,
    status VARCHAR(50) NOT NULL,
    anomaly BOOLEAN DEFAULT FALSE,
    severity VARCHAR(50) DEFAULT 'LOW',
    anomaly_type VARCHAR(255) DEFAULT 'normal_behavior',
    score DOUBLE DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO payments (id, order_id, amount, status, anomaly, severity, anomaly_type, score) VALUES
(101, 501, 249.99, 'SUCCESS', FALSE, 'LOW', 'normal_behavior', 0.12),
(102, 502, 12500.00, 'FAILED', TRUE, 'CRITICAL', 'Unusual High Amount', 0.94),
(103, 503, 89.50, 'SUCCESS', FALSE, 'LOW', 'normal_behavior', 0.08),
(104, 504, 4999.00, 'SUCCESS', TRUE, 'HIGH', 'Rapid Velocity', 0.81),
(105, 505, 34.00, 'SUCCESS', FALSE, 'LOW', 'normal_behavior', 0.05)
ON DUPLICATE KEY UPDATE amount=VALUES(amount), status=VALUES(status), anomaly=VALUES(anomaly);
