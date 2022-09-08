from datetime import datetime
from pytz import timezone


class CreateAccount:

    @staticmethod
    def date(self):
        ...

    def __init__(self, agency, num_account, balance, name, cpf):
        self.agency = agency
        self.num_account = num_account
        self._balance = balance
        self.name = name
        self.cpf = cpf
        self._limit = 0
        self.transfer = []

    def deposit(self, value):
        self._balance += value
        print(f"${value:.2f} deposited")

    def withdraw(self, value):
        if value > (self._balance - self._limit):
            print(f"Withdraw is not possible, your balance ${self._balance:.2f} is under limit ${self._limit:.2f}")
        else:
            self._balance -= value
            print(f"Balance: ${self._balance:.2f}")

    def switch(self, value, num_account):
        print(f"Transfering {value} to {num_account}")
        self.withdraw(value)
        num_account.deposit(value)

    def consult_balance(self):
        return print(f"Actual balance ${self._balance:.2f}, Account {self}")

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = -value
