def repeat(times):
    def deco(fn):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return deco

@repeat(3)
def ping():
    print("ping")

ping()
