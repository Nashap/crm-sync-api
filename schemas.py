from pydantic import BaseModel

class CampaignSchema(BaseModel):
    platform: str
    campaign_name: str
    impressions: int
    clicks: int
    spend: float

    class Config:
        orm_mode = True