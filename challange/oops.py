from bank_account import *

Ali = BankAccount(1000, "Ali")
Sara = BankAccount(2000, "Sara")


Ali.get_balance()
Sara.get_balance()

# Sara.deposit(500)

# Ali.withdraw(1000)

Ali.transfer(500, Sara)
Sara.get_balance()

Ik=InterestRewardsAcct(1000, "Ik")
Ik.get_balance()
Ik.deposit(500)

Ik.transfer(500, Sara)
Sara.get_balance()


Khan = SavingsAcct(1000, "Khan")

Khan.get_balance()

Khan.deposit(100)

Khan.transfer(10000, Sara)
Khan.transfer(1000, Sara)