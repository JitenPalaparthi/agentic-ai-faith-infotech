class Employee:
    company = "ACME"
    def __init__(self, name):
        self.name = name

a = Employee("A")
b = Employee("B")
print(a.company, b.company)
