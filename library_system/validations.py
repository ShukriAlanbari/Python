class Validation:
        @staticmethod
        def validate_ISBN(value) -> bool:
            if isinstance(value, str) and len(value) == 13:
                return True
            else:
                print("[i] Invalid input. Has to be 13 numbers")
                return False
        
        
        
        @staticmethod
        def validate_book_title(book_title):
            if len(book_title) > 0:
                return True
            else:
                return False
        
        
        
        @staticmethod
        def validate_is_alnum(value: str):
            if isinstance(value,str) and value.isalnum():
                return True
            else:
                print("[i] Invalid input")
                return False
        
        
        
        
        @staticmethod
        def read_in_int_value(validation_function, message:str):
            while True:
                user_input = input(message)
                if user_input.isnumeric() and validation_function(int(user_input)):
                    return int(user_input)



        @staticmethod
        def read_in_value(validation_function,message:str):
            while True:
                user_input = input(message)
                if validation_function(user_input):
                    return user_input

        @staticmethod
        def validate_str_alpha(value:str):
            if isinstance(value, str) and value.replace(" ","").isalpha():
                return True
            else:
                return False
            
            
            
        @staticmethod
        def validate_mob_num(value:str):
            if isinstance(value, str) and value.strip().isnumeric() and value.startswith("07") and len(value) == 10:
                return True
            else:
                print("\n[i] Invalid mobile number (07xxxxxxxx)\n")
                return False
            
            
            
        @staticmethod
        def valid_id(value:str):
            if isinstance(value, str) and len(value) == 4:
                return True
            else:
                return False