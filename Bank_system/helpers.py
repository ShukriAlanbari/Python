import random
import datetime

class Helpers():
    
    # Method to randomize a card number of 16 digits
    @staticmethod
    def random_card_num(unique_card_list: list):
        while True:
            random_pt_1 = str(random.randint(0000,9999))
            random_pt_2 = str(random.randint(0000,9999))
            random_pt_3 = str(random.randint(0000,9999))
            random_pt_4 = str(random.randint(0000,9999))
            
            card_num = f"{random_pt_1}-{random_pt_2}-{random_pt_3}-{random_pt_4}"
            if card_num not in unique_card_list:
                unique_card_list.append(card_num)
                break
            else:
                continue
            
        return card_num


    # Method to randomize a PIN of 4 digits    
    @staticmethod
    def random_pin():
        random_pin = str(random.randint(0000,9999))
        return random_pin
    

    # Method to randomize a CVC code of 3 digits
    @staticmethod
    def random_sec_code() -> str:
        random_sec_code = str(random.randint(000,999))
        return random_sec_code
    
    
    # Method to generate a valid month
    @staticmethod
    def val_month():
        valid_month = random.choice(range(1, 13))
        return valid_month
    
    
    # Method to generate a valid year using datetime
    @staticmethod
    def val_yr():
        current_year = datetime.datetime.now().year
        valid_year = current_year + 5
        return valid_year
    
    
    # Method to generate a random and unique ID number
    @staticmethod
    def random_id(unique_id_list: list):
        while True:
            random_id = str(random.randint(100000,999999))
            if random_id not in unique_id_list:
                unique_id_list.append(random_id)
                break
            else:
                continue     
        return random_id



    # Method to generate an account number
    @staticmethod
    def random_acc_num(unique_acc_list):
        while True:
            random_pt_1 = str(random.randint(0000,9999))
            random_pt_2 = str(random.randint(0000,9999))
            random_pt_3 = str(random.randint(0000,9999))
            
            acc_num = f"{random_pt_1}-{random_pt_2}-{random_pt_3}"
            if acc_num not in unique_acc_list:
                unique_acc_list.append(acc_num)
                break
            else:
                continue     
        return acc_num