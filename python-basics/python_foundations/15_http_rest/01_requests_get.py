import requests
r = requests.get("https://httpbin.org/get", timeout=5)
print(r.status_code)
print(r.json()["url"])
