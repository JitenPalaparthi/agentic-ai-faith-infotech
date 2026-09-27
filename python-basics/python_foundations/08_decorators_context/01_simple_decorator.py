def trace(fn):
    def wrapper(*args, **kwargs):
        print("calling", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@trace
def add(a, b):
    return a + b

print(add(2, 3))
