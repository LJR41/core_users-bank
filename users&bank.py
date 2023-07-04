class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()

class BankAccount:
    acc_balance = 0
    def_interest = 0.01

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount
        return self

    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.acc_balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.acc_balance}")    
    
    def yield_interest(self):
        if self.acc_balance > 0:
            self.acc_balance * self.int_rate
        return self
    
josh = User("Josh", "yahoo@yehaw.com")

josh.make_deposit(500)

josh.make_withdrawal(250)

josh.display_user_balance()