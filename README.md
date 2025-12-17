# 🥇 Gold & Silver Price Monitoring – End-to-End Data Pipeline

This project demonstrates a **production-style end-to-end data pipeline** that fetches real-time **Gold and Silver prices**, stores them reliably in a SQL database, exposes the data via a **Flask API**, and visualizes it using **Streamlit**, with **monitoring, logging, automation, and Docker support**.

The focus is on **reliability, observability, and automation**, not UI complexity.

---

## 📌 Architecture Overview

```
GoldAPI (External API)
        ↓
Python Pipeline (ETL)
        ↓
SQLite Database
        ↓
Flask Backend API
        ↓
Streamlit Dashboard
        ↓
Monitoring & Logs
```

---

## 🛠 Tech Stack

* **Language:** Python 3.12
* **External API:** GoldAPI.io
* **Database:** SQLite
* **Backend:** Flask
* **Dashboard:** Streamlit
* **Logging:** Python logging module
* **Containerization:** Docker & Docker Compose
* **OS:** Windows (local), Linux-ready

---

## 📊 Data Source

**GoldAPI.io**

* Real-time precious metal prices
* Gold (XAU) and Silver (XAG)
* Secure API access using headers

Example:

```http
GET https://www.goldapi.io/api/XAU/USD
x-access-token: <API_KEY>
```

---

## 📁 Project Structure

```
gold-silver-pipeline/
│
├── pipeline/
│   └── fetch_prices.py        # Extract → Transform → Store
│
├── backend/
│   └── app.py                 # Flask API
│
├── dashboard/
│   └── app.py                 # Streamlit dashboard
│
├── data/
│   └── metals.db              # SQLite database
│
├── logs/
│   └── error.log              # Error & pipeline logs
│
├── .env                       # API keys & config
├── requirements.txt
└── README.md
```

---

## 🔄 Data Pipeline Flow

### 1️⃣ Extraction

* Fetches Gold (XAU) and Silver (XAG) prices from GoldAPI
* Uses API token from environment variables
* Handles timeouts, SSL errors, and API failures

### 2️⃣ Transformation

* Normalizes fields
* Extracts price, currency, timestamp
* Ensures consistent schema for storage

### 3️⃣ Storage

* Stores prices in SQLite
* Prevents duplicates
* Maintains update timestamps

---

## 🚦 Monitoring & Reliability

### Implemented Monitoring

* ✅ Error logging to `logs/error.log`
* ✅ Pipeline failure tracking
* ✅ Timestamped updates
* ✅ Safe re-runs without data corruption

### Example Log Entry

```
2025-12-16 21:20:22 - API timeout while fetching gold prices
```

---

## 🌐 Backend API (Flask)

### Start Backend

```bash
python backend/app.py
```

### Health Check

```
GET http://127.0.0.1:5000/
```

Response:

```json
{
  "status": "Gold & Silver API is running"
}
```

### Prices Endpoint

```
GET /prices
```

Returns latest metal prices from SQLite.

---

## 📈 Dashboard (Streamlit)

### Start Dashboard

```bash
streamlit run dashboard/app.py
```

Open:

```
http://localhost:8501
```

### Dashboard Features

* Live Gold & Silver prices
* Clean visualization
* Backend API integration
* Error visibility when backend is down

---

## ⚙️ Automation

### Local Automation (Windows)

Use **Task Scheduler** to run the pipeline periodically:

```bash
python pipeline/fetch_prices.py
```

### Production-Ready Options

* Cron jobs (Linux)
* GitHub Actions (scheduled workflows)
* Azure Functions / AWS Lambda
* n8n workflows

---

## 🔐 Environment Variables

Create `.env` file:

```env
GOLD_API_KEY=your_goldapi_key_here
```

---

## 🚀 Scaling & Production Improvements

If this system were deployed to production, improvements would include:

* Replace SQLite with PostgreSQL
* Add retries with exponential backoff
* Centralized logging (ELK / Azure Monitor)
* Alerting via Slack or Email
* API authentication & rate limiting
* CI/CD pipeline with GitHub Actions
* Container orchestration (Kubernetes)

---

## ✅ Key Takeaways

* End-to-end automated pipeline
* Real-world API integration
* Monitoring & failure visibility
* Clean separation of concerns
* Dockerized, scalable architecture

---
