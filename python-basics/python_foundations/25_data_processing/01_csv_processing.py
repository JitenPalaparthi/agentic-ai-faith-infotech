import csv
from io import StringIO
text = "name,score\nA,10\nB,20\n"
rows = list(csv.DictReader(StringIO(text)))
print(sum(int(r["score"]) for r in rows))
