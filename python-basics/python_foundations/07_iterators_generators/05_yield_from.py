def part():
    yield 1
    yield 2

def whole():
    yield 0
    yield from part()
    yield 3

print(list(whole()))
