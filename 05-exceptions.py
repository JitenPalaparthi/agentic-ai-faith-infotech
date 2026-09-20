# divide by zero

try:
    print(10/0)
except ZeroDivisionError as e:
    print("handled:",e)
finally:
    print("done with success or failure")


class InvalidAgeError(ValueError):
    pass

# class A:B{}

def validate(age):
    if age<0:
        raise InvalidAgeError("age can not be be negative")
        # throw
try:
    validate(10)
    validate(-10)
    print("age is successfully validated")
except InvalidAgeError as e: # catch
    print(e)