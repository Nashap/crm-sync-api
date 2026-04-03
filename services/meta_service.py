import requests

META_TOKEN = "YOUR_META_ACCESS_TOKEN"
AD_ACCOUNT_ID = "act_xxxxx"

def fetch_meta_campaigns():
    url = f"https://graph.facebook.com/v18.0/{AD_ACCOUNT_ID}/campaigns"
    
    params = {
        "access_token": META_TOKEN,
        "fields": "name,insights{impressions,clicks,spend}"
    }

    response = requests.get(url, params=params)
    return response.json()