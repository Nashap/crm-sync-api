# CRM Sync API

A FastAPI-based backend system to integrate and normalize advertising data from multiple platforms like Meta (Facebook/Instagram), Google, and LinkedIn.

---

## 🚀 Features

- Multi-platform API integration
- Data normalization (common format)
- SQLite database storage
- REST API endpoints for syncing data
- Environment variable support using `.env`
- Basic error handling for API failures
- WhatsApp lead sync endpoint

---

## 🧠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Requests
- python-dotenv

---

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



---

## 📬 API Endpoints

### 🔄 Sync APIs

- `POST /sync/meta` → Fetch & store Meta data
- `POST /sync/google` → Fetch & store Google data
- `POST /sync/linkedin` → Fetch & store LinkedIn data

### 📲 Additional API

- `POST /sync/whatsapp` → Receive lead data

---

## 🔄 Data Flow

1. API request is received
2. Data is fetched from external platforms
3. Data is normalized into a common format
4. Data is stored in the database
5. Response is returned

---

## 📊 Output

Data is stored in SQLite database (`crm.db`) with:

- platform
- campaign_name
- impressions
- clicks
- spend

---

## 🔐 Notes

- Meta & LinkedIn APIs require access tokens
- Tokens are stored securely using `.env`
- Google data currently uses sample API (can be replaced with GA4)

---

## 👨‍💻 Author

Nasha P


