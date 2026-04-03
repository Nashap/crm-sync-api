from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.google_service import fetch_google_data
from utils.normalizer import normalize_google
from models import Campaign

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/sync/google")
def sync_google(db: Session = Depends(get_db)):
    raw = fetch_google_data()

    for c in raw:
        norm = normalize_google(c)

        campaign = Campaign(**norm)
        db.add(campaign)

    db.commit()
    return {"status": "Google synced"}