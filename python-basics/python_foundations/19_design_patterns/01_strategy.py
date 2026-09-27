from typing import Protocol

class Pricing(Protocol):
    def price(self, total: float) -> float: ...

class Regular:
    def price(self, total): return total

class Discount:
    def price(self, total): return total * 0.9

def checkout(total, pricing: Pricing):
    return pricing.price(total)

print(checkout(100, Discount()))
