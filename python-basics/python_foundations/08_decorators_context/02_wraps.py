from functools import wraps

def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@trace
def hello():
    "demo docstring"
    return "hi"

print(hello.__name__, hello.__doc__)
