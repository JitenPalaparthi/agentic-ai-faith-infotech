import requests
payload = {"name": "Ada"}
r = requests.post("https://httpbin.org/post", json=payload, timeout=5)
print(r.json()["json"])
