import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")