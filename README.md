# 🔌 Laptop Price Prediction API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

> Production-ready REST API for laptop price prediction — FastAPI + Docker containerized ML model serving with structured endpoints.

---

## 📌 Overview

This repo serves the laptop price prediction model as a REST API using FastAPI, containerized with Docker for consistent and scalable deployment.

---

## ✨ Key Features

- ✅ **FastAPI** REST API with auto-generated Swagger docs
- ✅ **Docker** containerized for easy deployment
- ✅ Clean request/response schema with Pydantic validation
- ✅ Streamlit frontend for interactive UI

---

## 📁 Project Structure

```
laptop-price-prediction-api/
├── app/                    # FastAPI application
├── model/                  # Trained ML model files
├── data/                   # Dataset
├── src/                    # Feature engineering
├── notebooks/              # EDA & training notebooks
├── streamlit_app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/MishraAbhay03/laptop-price-prediction-api.git
cd laptop-price-prediction-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger UI.

### Docker

```bash
docker build -t laptop-price-api .
docker run -p 8000:8000 laptop-price-api
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/predict` | Predict laptop price |
| GET | `/docs` | Swagger UI |

---

## 👤 Author

**Abhaykumar Mishra** — [GitHub](https://github.com/MishraAbhay03) · [LinkedIn](https://www.linkedin.com/in/abhaykumar-mishra-791a38300)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
