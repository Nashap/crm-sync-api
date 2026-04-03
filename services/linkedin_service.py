import requests

LINKEDIN_TOKEN = "YOUR_LINKEDIN_TOKEN"

def fetch_linkedin_campaigns():
    url = "https://api.linkedin.com/v2/adCampaignsV2"

    headers = {
        "Authorization": f"Bearer {LINKEDIN_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()