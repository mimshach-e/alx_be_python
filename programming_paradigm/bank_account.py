# Programming Paradigms & Exception handling
# Task 0 - Create a Simple Bank Account Class

# Class Definition
class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance


# Encapsulation and Behaviors
    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount < self.account_balance:
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

