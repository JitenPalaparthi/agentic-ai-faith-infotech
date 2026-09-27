from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Expense:
    category: str
    amount: float

expenses = [
    Expense("food", 120),
    Expense("travel", 350),
    Expense("food", 80),
]
totals = defaultdict(float)
for e in expenses:
    totals[e.category] += e.amount
print(dict(totals))
