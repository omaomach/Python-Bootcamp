import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta

load_dotenv()
API_KEY = os.environ.get("NEWSAPI_KEY")

if not API_KEY:
    print("NEWSAPI_KEY is not set. Did you create .env and call load_dotenv()?")
    raise SystemExit(1)

query = input("What are you interested in today? ")

DAYS_BACK = 7
from_date = (date.today() - timedelta(days=DAYS_BACK)).isoformat()

url = "https://newsapi.org/v2/everything"
params = {
    "q": query,
    "from": from_date,
    "sortBy": "publishedAt",
    "apiKey": API_KEY,
}

try:
    response = requests.get(url, params=params, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    raise SystemExit(1)

try:
    data = response.json()
except ValueError:
    print(f"Response was not valid JSON (HTTP {response.status_code}):")
    print(response.text[:500])
    raise SystemExit(1)

if data.get("status") != "ok":
    print(f"API error (HTTP {response.status_code}): {data.get('code')} — {data.get('message')}")
    raise SystemExit(1)

articles = data.get("articles", [])
if not articles:
    print("No articles found for that query.")
    raise SystemExit(0)

for index, article in enumerate(articles):
    print(index + 1, article.get("title"))
    print(article.get("url"))
    print("\n*******************************************************\n")
