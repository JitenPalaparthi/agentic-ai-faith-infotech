from itertools import groupby
items = sorted([("IT","A"),("HR","B"),("IT","C")])
for dept, group in groupby(items, key=lambda x:x[0]):
    print(dept, [x[1] for x in group])
