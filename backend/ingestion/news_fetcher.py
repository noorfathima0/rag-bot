import requests
import os
from dotenv import load_dotenv

load_dotenv()
EXA_API_KEY = os.getenv("EXA_API_KEY")

def fetch_news_from_exa(domain="general"):
    headers = {
        "Authorization": f"Bearer {EXA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": f"latest {domain} India",
        "numResults": 10
    }
    response = requests.post("https://api.exa.ai/search", headers=headers, json=payload)
    results = response.json().get("results", [])
    return [
        {
            "title": r["title"],
            "content": r["text"],
            "url": r["url"],
            "publishedAt": r.get("publishedDate", "")
        } for r in results
    ]
