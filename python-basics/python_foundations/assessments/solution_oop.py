class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("positive amount required")
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance: raise ValueError("insufficient funds")
        self.balance -= amount
