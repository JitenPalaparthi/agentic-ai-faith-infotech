import copy
a = [[1], [2]]
b = a.copy()
c = copy.deepcopy(a)
a[0].append(99)
print("a:", a)
print("shallow:", b)
print("deep:", c)
