import os
from dotenv import load_dotenv
import requests

load_dotenv()

GOOGLE_TOKEN = os.getenv("GOOGLE_TOKEN")
GOOGLE_CUSTOMER_ID = os.getenv("GOOGLE_CUSTOMER_ID")


def fetch_google_data():
    try:
        url = f"https://googleads.googleapis.com/v14/customers/{GOOGLE_CUSTOMER_ID}/googleAds:search"

        headers = {
            "Authorization": f"Bearer {GOOGLE_TOKEN}",
            "Content-Type": "application/json"
        }

        query = {
            "query": "SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros FROM campaign"
        }

        res = requests.post(url, headers=headers, json=query)
        res.raise_for_status()

        return res.json()

    except Exception as e:
        return {"error": str(e)}