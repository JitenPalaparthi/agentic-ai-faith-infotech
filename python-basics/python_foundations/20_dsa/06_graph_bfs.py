from collections import deque
g = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
seen = {"A"}
q = deque(["A"])
while q:
    n = q.popleft()
    print(n)
    for nxt in g[n]:
        if nxt not in seen:
            seen.add(nxt); q.append(nxt)
