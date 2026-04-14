import os
from dotenv import load_dotenv
import requests

load_dotenv()

LINKEDIN_TOKEN = os.getenv("LINKEDIN_TOKEN")


def fetch_linkedin_campaigns():
    try:
        url = "https://api.linkedin.com/v2/adCampaignsV2"

        headers = {
            "Authorization": f"Bearer {LINKEDIN_TOKEN}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    except Exception as e:
        return {"error": str(e)}