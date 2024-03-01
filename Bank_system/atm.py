from bankaccount import BankAccount as BA, CreditBankAccount as CBA
from bankcards import BankCard as BC
from validation import Validations as Vald

#registered_users = []

# 'FrontEnd' class
class Atm():

    acc_db = {}
    acc_cr_db = {}
    new_bank_card_db = {}
    amount = 0
    
    """
    # DEMO ###################
    demo_man_deb = BA(owner_name="Mr Test")
    
    demo_man_cr = CBA(owner_name=demo_man_deb.owner_name)
    demo_man_cr.set_cr_limit()
    demo_man_cr.set_cr_interest_percent()
    
    demo_card = BC(connected_bank_acc=demo_man_deb, connected_cr_bank_acc=demo_man_cr)
    # DEMO ###################
    
    acc_db[demo_man_deb.id] = demo_man_deb
    acc_cr_db[demo_man_cr.id] = demo_man_cr
    new_bank_card_db[demo_card] = demo_card
    
    # DEMO ###################
    def demo_str(d_m_d: BA, d_m_c: CBA, d_c: BC):
        return f"BankAccount: {d_m_d.display()}"+\
            f"Credit Bank account: {d_m_c.display()}\n"+\
            f"Bank Card: {d_c.__str__()}\n"
    # DEMO ###################
    """
    
    #Menu
    def show_main_menu():
        PROMPT_MENU = \
        '''Welcome to -[ $camBank AB ]-: 

[1]  Login
[2]  Register account
[3]  Exit

        '''
        
        return PROMPT_MENU
    
    #Sub Menu
    def show_sub_login_menu():
        SUB_LOGIN_MENU =\
        """
[1]  Withdrawal
[2]  Deposit
[3]  Check balance
[4]  Logout
    """
        return SUB_LOGIN_MENU
                    
    #Calls for withdrawal
    def withdraw(bank_card: BC, deb_acc: BA, cr_acc: CBA, amount):
        bank_card.wd_choice(deb_acc=deb_acc, cr_acc=cr_acc ,amount=amount)
    
    #Calls for specific deposit
    def deposit(db_user: BA, cr_user: CBA):
        while True:
            print(f"\n[1]: Debit\n[2]: Credit\n[3]: Go Back")
            choice = input("\n[?] Please choose one of the options above ->: ")
            
            if choice == "1":
                amount = int(input("\n[?]: How much would you like to deposit ->: "))
                db_user.deposit(amount)
                break
            
            elif choice == "2":
                amount = int(input("[?]: How much would you like to deposit ->: "))
                cr_user.cr_deposit(amount)
                break
                
            elif choice == "3":
                print(f"[i]: Going back...")
                break
                        
            else:
                print(f"\nPlease choose from the list")
    
    #Gets deb. balance
    def get_balance_debit(user: BA):
        balance = user.balance
        return balance
    
    #Gets cred. balance
    def get_balance_cr(user: CBA):
        balance = user.cr_balance
        return balance
    
    #Displays available funds
    def display_funds(deb_balance, cr_balance,  cr_acc: CBA):
        print(f"\n[1]: Debit\n[2]: Credit\n[3]: Both")
        choice = input("\n[?] Please choose one of the options ->: ")
        
        if choice== "1":     
            return f"\n[i] Available funds: {deb_balance}SEK"
            
        elif choice== "2":
            return f"\n[i] Used credit : {cr_balance}SEK out of {cr_acc.cr_limit}SEK"
        
        elif choice == "3":
            return f"\n[i] Available debit funds: {deb_balance}SEK" +\
                f"\n    Used Credit funds: {cr_balance}SEK out of {cr_acc.cr_limit}SEK\n"
            

    def reg_acc(acc_db, acc_cr_db, my_bank_card_db):
        first_name = Vald.read_in_value(Vald.validate_str_alpha,
                                         "Enter your First Name: ")
        last_name = Vald.read_in_value(Vald.validate_str_alpha,
                                         "Enter Your Last Name: ")

        owner_name = f"{first_name} {last_name}"
        new_acc = BA(owner_name=owner_name)
        
        new_cr_acc = CBA(owner_name=owner_name)
        new_cr_acc.cr_limit = new_cr_acc.set_cr_limit()
        new_cr_acc.cr_interest_percent = new_cr_acc.set_cr_interest_percent()
        
        acc_db[new_acc.id] = new_acc
        acc_cr_db[new_cr_acc.id] = new_cr_acc
        
        my_bank_card = BC(connected_bank_acc=new_acc, connected_cr_bank_acc=new_cr_acc)
        
        my_bank_card_db[my_bank_card.card_number] = my_bank_card
        
        # registered_users.append({
        # 'id': new_acc.id,
        # 'account': new_acc,
        # 'credit_account': new_cr_acc,
        # 'card': my_bank_card
        # })
        
        print(f"\n[i]: New accounts created for {owner_name}")
        print(new_acc.display())
        print(f"[i]: A new bankcard will arrive within 2-5 bankdays\n")

        # return new_acc, new_cr_acc, my_bank_card

    def login(acc_db: dict, acc_cr_db:dict, amount) -> bool:
        #Checks if account in "database" and asks for id
        login_id = input(f"\n[?]: Please enter your id ->: ")
        
        if login_id in acc_db:
            acc = acc_db[login_id]
            cr_acc = acc_cr_db.get(login_id)
            
            if cr_acc is not None:
                my_bank_card = Atm.new_bank_card_db.get(cr_acc.card_number)
                
                while True:
                    print(f"\n[i]: Login Successful!")
                    while True:
                        print(Atm.show_sub_login_menu())
                        choice = input("\n[?]: Please choose ->: ")
                        
                        if choice == "1":
                            Atm.withdraw(my_bank_card, deb_acc=acc, cr_acc=cr_acc ,amount=amount)
                            continue
                        
                        elif choice == "2":
                            Atm.deposit(db_user=acc, cr_user=cr_acc)
                            continue
                                        
                        elif choice == "3":
                            deb_balance = Atm.get_balance_debit(acc)
                            cr_balance = Atm.get_balance_cr(cr_acc)
                            print(Atm.display_funds(deb_balance=deb_balance, cr_balance=cr_balance, cr_acc=cr_acc))

                        
                        elif choice == "4":
                            print(f"\n[i] Logging off...\n")
                            break
                        
                        else:
                            print(f"[!]: Choose from the list below.")
                    break
        else:
            print("[!]: User not found.")
                    
        # else:
        #     print(f"[i]: User not found!")
            
    def run():
        #print(Atm.demo_str(d_m_d=Atm.demo_man_deb, d_m_c=Atm.demo_man_cr, d_c=Atm.demo_card))
        while True:
            print(Atm.show_main_menu())
            user_choice = input("Your choice: ")
            if user_choice == "1":
                if len(Atm.acc_db) != 0:
                    Atm.login(acc_db=Atm.acc_db, acc_cr_db=Atm.acc_cr_db, amount=Atm.amount)
                else:
                    print("[i]: No users registered.")
            
            elif user_choice == "2":
                Atm.reg_acc(Atm.acc_db, Atm.acc_cr_db, Atm.new_bank_card_db)
            
            elif user_choice == "3":
                print(f"\n[i] Exiting program...\n")
                break