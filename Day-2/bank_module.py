"""A module containing a class and standalone functions, meant to be imported elsewhere."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def greet(name):
    return f"Hello, {name}!"


# Only runs when this file is executed directly (e.g. `python bank_module.py`),
# not when it is imported by another module.
if __name__ == "__main__":
    acc = BankAccount("Direct Run", 100)
    print(acc)
