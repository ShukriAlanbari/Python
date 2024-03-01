import re 



class Validations():
    
    @staticmethod
    def valid_id(value):
        pattern = r"^\d{10}$"
        return bool(re.match(pattern, value))
    
    @staticmethod
    def valid_name(value):
        pattern = r"^[A-Za-z]+ [A-Za-z]+$"
        return bool(re.match(pattern, value))

    @staticmethod
    def valid_company_name(value):
            return bool(re.match(".*[A-Za-z].*", value))

    @staticmethod
    def valid_address(value):
        parts = value.split()
        if len(parts) != 4:
            return False

        part1, part2, part3, part4 = parts

        if not (part1.isalnum() and part2.isalnum() and part3.isdigit() and part4.isalpha()):
            return False

        return True

  
    @staticmethod
    def valid_phone(value):
        return bool(re.match(r'^07\d{8}$', value))
    
    @staticmethod
    def valid_email(value:str):
        # Use a regular expression to validate the email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, value):
            return True
        else:
            return False
        
    @staticmethod
    def valid_password(value):
        return bool(re.match(r'^(?=.*[A-Z])(?=.*[!@#$%^&.*]).{8,}$', value))

    @staticmethod
    def valid_card_num(value:str):
         return bool(re.match(r'^\d{16}$', value))

    @staticmethod  
    def valid_account_num(value:str):
        return bool(re.match(r'^\d{20}$', value))

    @staticmethod
    def valid_vent_num(value:str):
        return bool(re.match (r"^\d{3}[A-Za-z]{3}$", value))

