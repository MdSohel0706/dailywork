import requests

payload = {"page" : 2, "count": 25}
r = requests.get("https://www.httpbin.org", params= payload)

print(r.url)