from collections import Counter, defaultdict, deque

print(Counter("mississippi"))

groups = defaultdict(list)
for name, dept in [("A", "IT"), ("B", "HR"), ("C", "IT")]:
    groups[dept].append(name)
print(dict(groups))

q = deque([1,2,3])
q.appendleft(0)
print(q)
