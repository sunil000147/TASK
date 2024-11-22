import requests
from config import SERPER_API_KEY
import sys
import os




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the API key
from config import SERPER_API_KEY


def research_industry(company_name, industry_name):
    """
    Fetch information about the company and industry.
    """
    search_query = f"{company_name} {industry_name} industry trends"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }
    response = requests.post(
        "https://google.serper.dev/search",
        headers=headers,
        json={"q": search_query},
    )

    if response.status_code != 200:
        return {"error": "Search API failed", "details": response.text}

    data = response.json()
    results = [
        {"title": item["title"], "snippet": item["snippet"], "link": item["link"]}
        for item in data.get("organic", [])[:5]  # Fetch top 5 results
    ]
    return results