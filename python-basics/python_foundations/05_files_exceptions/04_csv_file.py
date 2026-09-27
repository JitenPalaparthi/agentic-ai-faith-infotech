import csv
from io import StringIO

buf = StringIO()
writer = csv.writer(buf)
writer.writerow(["name", "score"])
writer.writerow(["Ada", 95])
print(buf.getvalue())
