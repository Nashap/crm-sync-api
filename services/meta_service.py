import os
from dotenv import load_dotenv
import requests

load_dotenv()

META_TOKEN = os.getenv("META_TOKEN")
AD_ACCOUNT_ID = os.getenv("AD_ACCOUNT_ID")


def fetch_meta_campaigns():
    try:
        url = f"https://graph.facebook.com/v18.0/{AD_ACCOUNT_ID}/campaigns"

        params = {
            "access_token": META_TOKEN,
            "fields": "name,insights{impressions,clicks,spend}"
        }

        res = requests.get(url, params=params)
        res.raise_for_status()

        return res.json()

    except Exception as e:
        return {"error": str(e)}