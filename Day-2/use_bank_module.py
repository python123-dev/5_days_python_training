"""Demonstrates importing a class and functions from bank_module.py."""

# Import specific names directly
from bank_module import BankAccount, add, multiply, greet

# Import the whole module (accessed as bank_module.<name>)
import bank_module

# --- Using the imported class ---
account = BankAccount("Alice", 500)
account.deposit(200)
account.withdraw(150)
print(account)

# --- Using imported functions directly ---
print("add(3, 4):", add(3, 4))
print("multiply(3, 4):", multiply(3, 4))
print(greet("Bob"))

# --- Using module-qualified access ---
print("bank_module.add(10, 20):", bank_module.add(10, 20))
second_account = bank_module.BankAccount("Charlie", 1000)
print(second_account)
