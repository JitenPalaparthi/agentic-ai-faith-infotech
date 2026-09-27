from functools import partial
power = lambda base, exp: base ** exp
square = partial(power, exp=2)
print(square(6))
