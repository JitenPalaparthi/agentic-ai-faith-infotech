def multiplier(factor):
    def inner(value):
        return value * factor
    return inner

double = multiplier(2)
print(double(10))
