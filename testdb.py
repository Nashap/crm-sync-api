from database import SessionLocal
from models import Campaign

db = SessionLocal()

data = db.query(Campaign).all()

for c in data:
    print(c.platform, c.campaign_name, c.clicks)