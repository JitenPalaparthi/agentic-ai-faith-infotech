class InvalidAgeError(ValueError):
    pass

def validate(age):
    if age < 0:
        raise InvalidAgeError("age cannot be negative")

def demo():
    pass

try:
    demo()
    validate(-1)
except InvalidAgeError as e:
    print(e)

