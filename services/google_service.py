import requests

def fetch_google_data():
    try:
        url = "https://dummyjson.com/products"  

        response = requests.get(url)
        response.raise_for_status()

        data = response.json().get("products", [])

        result = []
        for item in data[:5]:
            result.append({
                "campaign": item["title"],
                "impressions": 1000,
                "clicks": 100,
                "cost": 50
            })

        return result

    except Exception as e:
        return {"error": str(e)}