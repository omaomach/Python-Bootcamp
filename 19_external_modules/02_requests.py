import requests # This is a package that can get you html, txt, or JSON data from URLs. Its essential for interacting with web apis

r = requests.get('https://api.github.com/users/omaomach')

if r.status_code == 200:
    data = r.json()
    print(data['name'])
else:
    print(f"Error: {r.status_code}")

with open ("omaomach.txt", "w") as f:
    f.write(r.text)


# https://requests.readthedocs.io/en/latest/user/quickstart/