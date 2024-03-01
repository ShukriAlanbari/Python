from validations import Validation as Vald


class Borrower:
    
    def __init__(self,first_name:str,
                 last_name:str,
                 mobile_number:str,
                 id:str) -> None:
        try:    
            if Vald.validate_str_alpha(first_name):
                self.first_name = first_name
            else:
                raise ValueError("[i] Bad value - Enter your First name")
            if Vald.validate_str_alpha(first_name):
                self.last_name = last_name
            else:
                raise ValueError("[i] Bad value - Enter your Last name")
            if Vald.validate_mob_num(mobile_number):
                self.mobile_number = mobile_number
            else:
                raise ValueError("[i] Bad value - Mobile number")
            if Vald.valid_id(id):
                self.id = id
            else:
                raise ValueError("[i] Bad Value - ID")
            
            #A list where the borrowed book(s) will be stored
            self.borrowed_books = list()
            
        except Exception as error:
            print(error)
            
class Student(Borrower):
    def __init__(self, first_name, last_name, mobile_number, id) -> None:
        super().__init__(first_name, last_name, mobile_number, id)
        self.id_type = "S"
        self.id = self.id_type + id
        self.full_name = first_name.capitalize() +" "+ last_name.capitalize()
        self.mobile_number = mobile_number
        
    def __str__(self):
        return (f"Student: {self.full_name}\n"
                f"Mobile Number: {self.mobile_number}\n"
                f"Your ID: {self.id}")

class Teacher(Borrower):
    def __init__(self, first_name, last_name, mobile_number, id) -> None:
        super().__init__(first_name, last_name, mobile_number, id)
        self.id_type = "T"
        self.id = self.id_type + id
        self.full_name = first_name.capitalize() +" "+ last_name.capitalize()
        self.mobile_number = mobile_number
        
    def __str__(self):
        return (f"Teacher: {self.full_name}\n"
                f"Mobile Number: {self.mobile_number}\n"
                f"Your ID: {self.id}")