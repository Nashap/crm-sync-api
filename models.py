from sqlalchemy import Column, Integer, String, Float
from database import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    campaign_name = Column(String)
    impressions = Column(Integer)
    clicks = Column(Integer)
    spend = Column(Float)