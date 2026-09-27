def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

g = accumulator()
print(next(g))
print(g.send(10))
print(g.send(5))
