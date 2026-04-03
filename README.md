# CRM Sync API

A FastAPI-based backend system to integrate and normalize advertising data from multiple platforms like Meta (Facebook/Instagram), Google, and LinkedIn.

## 🚀 Features
- Multi-platform API integration
- Data normalization (common format)
- SQLite database storage
- REST API endpoints for syncing data

## 🧠 Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Requests

## 📁 Project Structure
crm_sync/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── services/
├── routes/
├── utils/


## ⚙️ Setup

1. Install dependencies:
pip install fastapi uvicorn sqlalchemy requests python-dotenv


2. Run server:
uvicorn crm_sync.main:app --reload

3. Open API docs:
http://127.0.0.1:8000/docs


## 📬 API Endpoints

- `/sync/meta` → Fetch & store Meta data
- `/sync/google` → Fetch & store Google data
- `/sync/linkedin` → Fetch & store LinkedIn data

## 📊 Output

Data is stored in SQLite database (`crm.db`) with normalized structure:
- platform
- campaign_name
- impressions
- clicks
- spend

---

## 📌 Note
- Meta & LinkedIn APIs require access tokens
- Google data is currently mocked for testing

---

## 👨‍💻 Author
Nasha P

