import json
text = '[{"name":"A","active":true},{"name":"B","active":false}]'
data = json.loads(text)
print([x["name"] for x in data if x["active"]])
