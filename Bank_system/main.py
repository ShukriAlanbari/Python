from atm import Atm
from bankaccount import BankAccount, CreditBankAccount
from bankcards import BankCard

if __name__ == "__main__":
    #Atm.run()
    Ba1 = BankAccount(owner_name="Erik Larsson")
    print(Ba1.display())
    
    Ba1.deposit(10000)
    print(Ba1.display())
    
    Ba1.withdraw(5000)
    print(Ba1.display())
    
    
    Cba1 = CreditBankAccount(owner_name="Erik Larsson")
    Cba1.set_cr_limit()
    print(Cba1.display())
    
    Bc1 = BankCard(connected_bank_acc=Ba1, connected_cr_bank_acc=Cba1)
    
    print(Bc1)
    
    Bc1.wd_from_both(Ba1, Cba1, 10000)