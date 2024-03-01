class Book:
    
    def __init__(self) -> None:
        self.student_price = 0
        self.teacher_price = 0
        self.fine = 0
        self.max_weeks_borrow = 0
        self.title = ""
        self.isbn = None
        self.is_borrowed = False
        self.borrower = None

class LiteraturBook(Book):
    def __init__(self, title:str) -> None:
        super().__init__()
        self.student_price = 0
        self.teacher_price = 10
        self.fine = 100
        self.max_weeks_borrow = 4
        if len(title) > 0:
            self.title = title
        else:
            print(f"[!]: Title cannot be empty..")
            
    
    def __str__(self) -> str:
        return f"Title: {self.title}\n"+\
                f"Max borrowtime (in weeks): {self.max_weeks_borrow}\n"+\
                f"Price for students: {self.student_price}\n"+\
                f"Price for Teachers: {self.teacher_price}\n"+\
                f"Delayed return fine: {self.fine}\n"
        
        
class ScienceBook(Book):
    def __init__(self, title:str) -> None:
        super().__init__()
        self.student_price = 5
        self.teacher_price = 15
        self.fine = 150
        self.max_weeks_borrow_student = 4
        self.max_weeks_borrow_teacher = 2
        if len(title) > 0:
            self.title = title
        else:
            print(f"[!]: Title cannot be empty..")
            
    def __str__(self) -> str:
        return f"Title: {self.title}\n"+\
                f"Max borrowtime students (in weeks): {self.max_weeks_borrow_student}\n"+\
                f"Max borrowtime teachers (in weeks): {self.max_weeks_borrow_teacher}\n"+\
                f"Price for students: {self.student_price}\n"+\
                f"Price for Teachers: {self.teacher_price}\n"+\
                f"Delayed return fine: {self.fine}\n"

class EntertainmentBook(Book):
    def __init__(self, title:str) -> None:
        super().__init__()
        self.fine = 50
        self.max_weeks_borrow = 3
        if len(title) > 0:
            self.title = title
        else:
            print(f"[!]: Title cannot be empty..")
            
            
    def __str__(self) -> str:
        return f"Title: {self.title}\n"+\
                f"Max borrowtime (in weeks): {self.max_weeks_borrow}\n"+\
                f"Price for students: {self.student_price}\n"+\
                f"Price for Teachers: {self.teacher_price}\n"+\
                f"Delayed return fine: {self.fine}\n"
            
            
"""         
världens_bästa_bok = EntertainmentBook(title="världens bästa bok")
världens_bästa_bok_2 = EntertainmentBook(title="")

print(världens_bästa_bok.__str__())
print(världens_bästa_bok_2.__str__())

"""