def normalize_meta(data):
    return {
        "platform": "meta",
        "campaign_name": data.get("name"),
        "impressions": int(data.get("impressions", 0)),
        "clicks": int(data.get("clicks", 0)),
        "spend": float(data.get("spend", 0)),
    }


def normalize_google(data):
    return {
        "platform": "google",
        "campaign_name": data.get("campaign"),
        "impressions": int(data.get("impressions", 0)),
        "clicks": int(data.get("clicks", 0)),
        "spend": float(data.get("cost", 0)),
    }


def normalize_linkedin(data):
    return {
        "platform": "linkedin",
        "campaign_name": data.get("name"),
        "impressions": int(data.get("impressions", 0)),
        "clicks": int(data.get("clicks", 0)),
        "spend": float(data.get("costInLocalCurrency", 0)),
    }