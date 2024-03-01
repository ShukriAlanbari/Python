from helpers import Helpers
from bankaccount import BankAccount as BA, CreditBankAccount as CBA


class BankCard():
    
    unique_card_list = []
    
    def __init__(self,
                connected_bank_acc: BA,
                connected_cr_bank_acc: CBA):
    
        self.card_number = Helpers.random_card_num(unique_card_list=BankCard.unique_card_list)
        
        self.pin_code = Helpers.random_pin()
        
        #Get from account
        self.owner_name = connected_bank_acc.owner_name
        
        self.security_code = Helpers.random_sec_code()
        
        self.val_month = Helpers.val_month()
        
        self.val_year = Helpers.val_yr()
        
        self.connected_bank_acc = connected_bank_acc
        
        self.connected_cr_bank_acc = connected_cr_bank_acc
        
    
    def __str__(self):
        # Prints out card information
        card_number_masked = "****-****-****-" + self.card_number[-4:]
        owner_name = self.owner_name
        valid_through = f"{self.val_month}/{self.val_year}"
        return f"\nCard Number: {card_number_masked}\n"\
            f"Card Holder: {owner_name}\nValid Through: {valid_through}\n"
    
    
    def wd_from_debit_card(self, deb_acc: BA, amount):
        # Takes Amount + D Fees and checks if available in debit acc balance.
        # Debit acc balance - (Amount + D Fees).
        if (amount + (amount * deb_acc.bank_fee))\
             <= deb_acc.balance:
            BA.withdraw(amount)
        else:
            print("[!]: Insufficient Debit Balance")
        
    def wd_from_cr_card(self, cr_acc: CBA, amount):
        # Takes Amount + C Fees and checks if available in credit account balance.
        total_withdrawal_amount = amount + (amount * cr_acc.bank_fee)
        if total_withdrawal_amount <= cr_acc.cr_limit - cr_acc.cr_balance:
            cr_acc.cr_withdraw(amount)
        else:
            print("Exceeds credit limit or insufficient funds for withdrawal.")
    
    def wd_from_both(self, deb_acc: BA, cr_acc: CBA, amount):
        # Makes a remaining amount from (Amount + D Fees) - Debit acc balance.
        # Checks if the remaining amount is available in Credit acc balance
        # Credit acc balance + remaining amount
        if (amount + (amount * deb_acc.bank_fee))\
             <= deb_acc.balance:
            deb_acc.withdraw(amount)
        else:
            remaining_amount = (amount + (amount * \
                deb_acc.bank_fee)) - deb_acc.balance
            
            if remaining_amount + (remaining_amount * cr_acc.bank_fee)\
                <= cr_acc.cr_limit - cr_acc.cr_balance:
                cr_acc.cr_withdraw(amount)
                
                print(f"Withdrew: {deb_acc.balance}SEK from Debit\n"
                    f"{remaining_amount}SEK from Credit")
                deb_acc.balance = 0
            else:
                print("[!]: Insufficient Balance In Both Accounts")
    
    def wd_choice(self, deb_acc:BA, cr_acc:CBA, amount):
        # Ask which account to draw funds from (or both)
        while True:
            choice = input("[1]: Debit\n[2]: Credit\n[3]: Both\n[4]: Go Back\n"
                    "\n[?]: Which option do you want to use? ").strip().lower()
            if choice == "debit" or choice == "1":
                amount = int(input("Enter the withdrawal amount: "))
                self.wd_from_debit_card(amount=amount, deb_acc=deb_acc)
                continue
            elif choice == "credit" or choice == "2":
                amount = int(input("Enter the withdrawal amount: "))
                self.wd_from_cr_card(amount=amount, cr_acc=cr_acc)
                continue
            elif choice == "both" or choice == "3":
                amount = int(input("Enter the withdrawal amount: "))
                self.wd_from_both(amount=amount, deb_acc=deb_acc, cr_acc=cr_acc)
                continue
            elif choice == "back" or choice == "4":
                print("[i]: Going back.")
                break
            else:
                print("[!]: Invalid Input")