import json
data = {"name": "Ada", "skills": ["Python", "SQL"]}
text = json.dumps(data, indent=2)
print(text)
print(json.loads(text))
