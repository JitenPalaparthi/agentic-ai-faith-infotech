class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, obj, owner):
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()
    def __init__(self, price):
        self.price = price

print(Product(10).price)
