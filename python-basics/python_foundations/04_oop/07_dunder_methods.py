class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"Money({self.amount})"

    def __add__(self, other):
        return Money(self.amount + other.amount)

print(Money(10) + Money(20))
