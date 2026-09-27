class Meta(type):
    def __new__(mcls, name, bases, ns):
        ns["created_by_meta"] = True
        return super().__new__(mcls, name, bases, ns)

class Demo(metaclass=Meta):
    pass

print(Demo.created_by_meta)
