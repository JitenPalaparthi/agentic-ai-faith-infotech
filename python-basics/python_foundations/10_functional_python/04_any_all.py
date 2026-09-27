values = [2,4,6]
print(all(x%2==0 for x in values))
print(any(x>5 for x in values))
