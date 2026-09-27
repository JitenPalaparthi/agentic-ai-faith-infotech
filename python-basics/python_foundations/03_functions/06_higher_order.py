def apply_twice(fn, value):
    return fn(fn(value))

print(apply_twice(lambda x: x * 2, 5))
