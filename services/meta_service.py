import os
from dotenv import load_dotenv
import requests

load_dotenv()

META_TOKEN = os.getenv("META_TOKEN")
AD_ACCOUNT_ID = "act_xxxxx"


def fetch_meta_campaigns():
    try:
        url = f"https://graph.facebook.com/v18.0/{AD_ACCOUNT_ID}/campaigns"

        params = {
            "access_token": META_TOKEN,
            "fields": "name,insights{impressions,clicks,spend}"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    except Exception as e:
        return {"error": str(e)}