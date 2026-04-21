from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.google_service import fetch_google_data
from models import Campaign

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sync/google")
def sync_google(db: Session = Depends(get_db)):
    raw = fetch_google_data()

    if "error" in raw:
        return raw

    for row in raw.get("results", []):
        campaign = row.get("campaign", {})
        metrics = row.get("metrics", {})

        db.add(Campaign(
            platform="google",
            campaign_name=campaign.get("name"),
            impressions=metrics.get("impressions"),
            clicks=metrics.get("clicks"),
            spend=metrics.get("cost_micros", 0) / 1_000_000
        ))

    db.commit()
    return {"status": "Google synced"}