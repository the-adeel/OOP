class BankAccount:
    def __init__(self, initial_balance = 0):
        self.initial_balance = initial_balance
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount should be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0 or amount < self.balance:
            raise ValueError("Invalid Input")        
        self.balance -= amount

    def __repr__(self):
        return f"A {self.__class__.__name__} Account with ${self.balance} in it."
class Savings(BankAccount):
    def pay_interest(self):
        self.balance += self.balance * 0.0035

class HighInterest(BankAccount):
    def __init__(self, withdraw_fee = 5):
        super().__init__()
        self.withdraw_fee = withdraw_fee

    def withdraw(self, amount):
        if amount < 0 or amount < self.balance:
            raise ValueError("Invalid Input")        
        self.balance -= (amount+self.withdraw_fee)

    def pay_interest(self):
        self.balance += self.balance * 0.007

class LockedIn(BankAccount):

    def withdraw(self, amount):
        raise ValueError("You can't withdraw on demand in this account type")

    def pay_interest(self):
        self.balance += self.balance * 0.009
