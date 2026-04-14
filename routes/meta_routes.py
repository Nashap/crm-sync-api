from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.meta_service import fetch_meta_campaigns
from utils.normalizer import normalize_meta
from models import Campaign

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sync/meta")
def sync_meta(db: Session = Depends(get_db)):
    raw = fetch_meta_campaigns()

    if "error" in raw:
        return {"status": "failed", "message": raw["error"]}

    for c in raw.get("data", []):
        insights = c.get("insights", {}).get("data", [{}])[0]

        norm = normalize_meta({
            "name": c.get("name"),
            "impressions": insights.get("impressions"),
            "clicks": insights.get("clicks"),
            "spend": insights.get("spend"),
        })

        db.add(Campaign(**norm))

    db.commit()
    return {"status": "Meta synced"}