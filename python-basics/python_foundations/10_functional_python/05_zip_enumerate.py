names = ["A", "B"]
scores = [90, 80]
print(list(zip(names, scores)))
for i, name in enumerate(names, start=1):
    print(i, name)
