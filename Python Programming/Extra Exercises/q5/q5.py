from bank_account import BankAccount

class CashAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.__balance = initial_balance
        self.withdrawl_count = 0

    def withdraw(self, amount):
        super().withdraw(amount)
        self.withdrawl_count += 1

    def deduct_monthly_fees(self):
        self.__balance -= self.withdrawl_count-4
        self.withdrawl_count = 0
        

