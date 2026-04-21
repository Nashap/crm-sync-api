from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.linkedin_service import fetch_linkedin_campaigns
from utils.normalizer import normalize_linkedin
from models import Campaign

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sync/linkedin")
def sync_linkedin(db: Session = Depends(get_db)):
    raw = fetch_linkedin_campaigns()

    if "error" in raw:
        return raw

    for c in raw.get("elements", []):
        norm = normalize_linkedin(c)
        db.add(Campaign(**norm))

    db.commit()
    return {"status": "LinkedIn synced"}