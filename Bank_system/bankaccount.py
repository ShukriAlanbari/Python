from validation import Validations as Vald
from helpers import Helpers


class BankAccount():
    
    unique_id_list = []
    unique_acc_list = []
    
    def __init__(self,
                owner_name: str) -> None:
        
        self.id = Helpers.random_id(unique_id_list=BankAccount.unique_id_list) #6 rand int in str
        self.acc_num = Helpers.random_acc_num(unique_acc_list=BankAccount.unique_acc_list) #12 rand int in str
        self.owner_name = owner_name #Str of fullname
        self.balance = 0 #Float of amount in format xxxx.xx
        self.bank_fee = 0.01 #Sets fee
    

   # A method to deposit money to debit account 
    def deposit(self, amount: float) -> str:
        self.balance += amount
        return f"[i]: {amount} added to balance!"


    # A method to withdraw money from debit account and apply fee
    def withdraw(self, amount: float):
        tot_amount = amount + (amount * self.bank_fee)
        cost = tot_amount - amount
        self.balance -= tot_amount
        return f"\n[i]: {amount} withdrawn from balance!\n"+\
            f"{cost} paid in fees\n"


    # A method to return information
    def display(self) -> str:
        return f"\nBank Account ID: [ {self.id} ]"+\
            f"\nBank Account Number: [ {self.acc_num} ]"+\
            f"\nBank Account Owner: [ {self.owner_name} ]"+\
            f"\nBalance in account: [ {self.balance} ]\n"

    
class CreditBankAccount(BankAccount):
    
    def __init__(self, owner_name) -> None:  
        super().__init__(owner_name)
        self.owner_name = owner_name
        self.cr_balance = 0
        self.cr_limit = None
        self.cr_interest_percent = None
        self.interest_cost_sum = None
        self.age = None
        self.bank_fee = 0.015


    # A method to decide credit limit for a person based on age
    def set_cr_limit(self):
        self.age = Vald.validate_age_int()
        if self.age < 18:
            print('You are to young')
            self.cr_limit = None
        elif 18 <= self.age < 25:
            self.cr_limit = 10000 #10k
        elif 25 <= self.age < 35:
            self.cr_limit = 25000 #25k
        elif 35 <= self.age < 50:
            self.cr_limit = 50000 #50k
        elif self.age >= 50:
            self.cr_limit = 150000 #150k

                      
    # A method to decide the intrest percent based on age from set_cr_limit
    def set_cr_interest_percent(self):      
        if self.age < 18:
            print('You are to young')
            self.cr_interest_percent = 0
        elif 18 <= self.age < 25:
            self.cr_interest_percent = 0.20 #20%
        elif 25 <= self.age < 35:
            self.cr_interest_percent = 0.10 #10%
        elif 35 <= self.age < 50:
            self.cr_interest_percent = 0.05 #5%
        elif self.age >= 50:
            self.cr_interest_percent = 0.01 #1%

        
    # A method deposit money to credit balance
    def cr_deposit(self, amount: float):
        if amount > 0:
            if amount <= self.cr_balance:
                self.cr_balance -= amount
                print(f"Deposited: {amount}SEK to credit balance.")
        else:
            print("Invalid amount to deposit.")

                  
    # A method to withdraw money from credit card + bank fee is applied
    def cr_withdraw(self, amount: float):
        bank_fee = 0.015
        if amount > 0:
            if amount <= self.cr_limit - self.cr_balance:
                self.cr_balance += amount
                bank_fee_drawn = bank_fee * amount
                print(f"Withdrew: {amount}SEK and a fee of {bank_fee_drawn}SEK has been applied.")
        else:
            print("Invalid amount of withdrawal.")

            
    # A method to apply the interest cost and calculate total sum
    def interest_cost(self):
        if self.cr_balance > 0:
            self.interest_cost_sum = (self.cr_balance * self.cr_interest_percent)
            
    
    def display(self) -> str:
        super().display()
        return f"\nCredit balance: {self.cr_balance}SEK"\
        f"\nCredit limit: {self.cr_limit}SEK"\
        f"\nInterest rate: {self.cr_interest_percent}%"\
        f"\nMonthly interest: {self.interest_cost_sum}SEK\n"