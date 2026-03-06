import requests # This is a package that can get you html, txt, or JSON data from URLs. Its essential for interacting with web apis

r = requests.get('https://api.github.com/users/omaomach')

with open ("omaomach.txt", "w") as f:
    f.write(r.text)