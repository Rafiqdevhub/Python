class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nAmount deposited: ${amount}")
        self.get_balance()
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Insufficient funds in account '{self.name}' to withdraw ${amount:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"\nAmount withdrawn: ${amount}")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
  
    def transfer(self, amount, recipient):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            recipient.balance += amount
            print(f"\nAmount transferred: ${amount} to account '{recipient.name}'")
            self.get_balance()
        except BalanceException as error:
            print(f'\nTransfer interrupted: {error}')
            

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount + (amount * 0.05)
        print(f"\nAmount deposited: ${amount}")
        self.get_balance()
        
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 0.05
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount+self.fee)
            self.balance -= amount
            print(f"\nAmount withdrawn: ${amount}")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')