import requests

query = input("What are you interested in today? ")
API_KEY = "81350c5faff7458b85fa7ee83955cbc0"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-12&sortBy=publishedAt&apiKey={API_KEY}"

print(url)

response = requests.get(url)
data = response.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"])
    print(article["url"])
    print("\n*******************************************************\n")
