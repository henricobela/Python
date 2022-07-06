class CreateAccount:

    def __init__(self, agency, num_account, balance, name, cpf):
        self.agency = agency
        self.num_account = num_account
        self.balance = balance
        self.name = name
        self.cpf = cpf

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def transf(self):
        pass

    def consult_balance(self):
        return self.balance


