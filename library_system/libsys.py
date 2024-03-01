
#######################################TODO####################################

#1- Validation for ISBN # Fixad /Eric --------------------------------------[X]
#2- Due date ---------------------------------------------------------------[/]
#3- Overdue ----------------------------------------------------------------[/]
#4- Funds ------------------------------------------------------------------[/]

#BUG:
#1- Cannot exit out of Login (does not accept x as input) ------------------[X]
#2- Add break to "borrowed" ------------------------------------------------[X]

###############################################################################

from book import LiteraturBook, ScienceBook, EntertainmentBook
from validations import Validation as Vald
from borrower import Borrower, Teacher, Student
import random


class LibSys():
    
    ### Attributes ###
    lib_books = {}
    book_id = 0
    teacher_db = {}
    student_db = {}
    id_input = ""

    ### Methods ###
    def show_main_menu():
        PROMPT_MENU = \
        '''Welcome to Libary, choose one of these options: 

[1] Register New User 
[2] LOGIN to library
[3] Add new book to library
[4] Reports
[5] Exit

        '''
        
        return PROMPT_MENU
        
    def register_user(choice:int, student_db:dict, teacher_db:dict):
        while True:
            try:
                print("\nChoose one of the options below!\n"
                    "1- Register a new Student.\n"
                    "2- Register a New Teacher.\n"
                    "3- Go back.\n")
        
                choice = int(input("Enter your choice: "))
                if choice in (1,2):
                    if choice == 1:
                        print("\nRegister a new Student:\n")
                    elif choice == 2:
                        print("\nRegister a new Teacher:\n")
                        
                    first_name = Vald.read_in_value(Vald.validate_str_alpha, 
                                                    "Enter your First Name: ")
                    last_name = Vald.read_in_value(Vald.validate_str_alpha, 
                                                "Enter your Last Name: ")
                    mobile_number = Vald.read_in_value(Vald.validate_mob_num, 
                                                    "Enter your mobile number: ")
                    random_numbers = [str(random.randint(0, 9)) for _ in range(4)]
                    id_num = ''.join(random_numbers)
                    
                    if choice == 1: # Student
                        new_student = Student(first_name=first_name,
                                            last_name=last_name,
                                            mobile_number=mobile_number,
                                            id=id_num)
                        print("\nStudent info:\n")
                        print(new_student)
                        print("\nRemember your ID!")
                        student_db[new_student.id] = new_student
                        input("\n[i]: Press enter to go back to start...\n")
                        break
                    elif choice == 2: # Teacher
                        new_teacher = Teacher(first_name=first_name,
                                            last_name=last_name,
                                            mobile_number=mobile_number,
                                            id=id_num)
                        print("\nTeacher info:\n")
                        print(new_teacher)
                        print("\nRemember your ID!")
                        teacher_db[new_teacher.id] = new_teacher
                        input("\n[i]: Press enter to go back to start...\n")
                        break
                    
                elif choice == 3:
                    break
                else:
                    print("[i] You need to choose an alternative from the list.")
                    continue
            except ValueError:
                print("[i] Please enter a valid integer choice.")    





    def login_menu(student_db:dict, teacher_db:dict, lib_books:dict, id_input:str):
        id_input = input("Enter your ID (\"x\" to go back): ") 
        while True:
            first_letter = id_input[0]
                # If Student "S"
            if id_input in student_db or teacher_db:
                print("\nLogin successful!\n")
                print("Personal Information:")
                if first_letter == "S":
                    print(student_db[id_input])
                elif first_letter == "T":
                    print(teacher_db[id_input])
                while True:
                    print("\nChoose one of the options below!\n"
                    "\n1- Borrow a new book.\n"
                    "2- Return a book.\n"
                    "3- Logout.\n")
                
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        LibSys.borrow_book(lib_books, id_input)
                        continue
                    elif choice == "2":
                        LibSys.return_borrowed_book(lib_books, id_input)
                        continue
                    elif choice == "3":
                        print(f"\n[i]: Logging out...\n")
                        break
                    else:
                        print("[i]: You need to choose an alternative from the list.")
                        continue
                break
            elif id_input.lower() == "x":
                break
            else:
                print("[i] User not found. Please check your ID.")
                continue
    
    def add_book_to_libary(lib_books, book_id):
        book_title = Vald.read_in_value(Vald.validate_book_title,\
            message= f"\nEnter title of book: ")
        isbn_num = Vald.read_in_value(Vald.validate_ISBN,\
            message= f"\nEnter ISBN number: ")
        
        book_name = (book_title + " " + str(book_id))
        book_id += 1
        
        while True:
            print(f"\nIn what category should we place this book?\n"+\
                f"\n[1]: Literature\n"+\
                f"[2]: Science\n"+\
                f"[3]: Entertainment\n")
            choice = input(f"Choose ->: \n")

            if choice in ("1", "2", "3"):
                if choice == "1":
                    book_name = LiteraturBook(book_title)
                    book_name.isbn = isbn_num
                    lib_books[book_title] = book_name
                    break
                
                elif choice == "2":
                    book_name = ScienceBook(book_title)
                    book_name.isbn = isbn_num
                    lib_books[book_title] = book_name    
                    break
                
                elif choice == "3":
                    book_name = EntertainmentBook(book_title)
                    book_name.isbn = isbn_num
                    lib_books[book_title] = book_name
                    break
                
            else:
                print(f"\n[!]: You need to choose an alternative from the list!\n")
                continue
                
        print(f'[i]: Book {book_title} was added to library!\n')





    def print_books_in_library(lib_books: dict):
        index = 1
        for key, book in lib_books.items():
            if hasattr(book, "title"):
                print(f"{index}: {book.title}")
                index += 1
            else:
                print(f"{index}: Title not found for {key}")

 
 
 
 
    def borrow_book(lib_books: dict, borrower: Borrower): #Add object to call attr.
        print("\n[i]: Select a book to borrow by entering its index")
        LibSys.print_books_in_library(lib_books)
        try:
            while True:
                book_index = Vald.read_in_value(Vald.validate_is_alnum,\
                message="Enter index of the book you want to borrow (\"X\" to cancel) ->: ")
                if book_index.lower() == "x":
                    print(f"[i]: Canceling...")
                    break
                elif book_index.isnumeric():
                    book_index = int(book_index)
                    if book_index >= 0 and book_index < len(lib_books):
                        book = list(lib_books.values())[book_index]
                        if not book.is_borrowed:
                            book.is_borrowed = True  
                            #book.borrower = student  
                            print(f"\n[i]: Book '{book.title}' has been borrowed by {borrower.id}.")
                            borrower.borrowed_books.append(book)
                            lib_books.pop(book) #Check functionality
                            break
                        else:
                            print(f"\n[i]: The book '{book.title}' is already borrowed.")
                    else:
                        print("\n[i]: Invalid book index. Please select a valid book.")
                        continue
                else:
                    print("\n[i]: Invalid input.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a valid book index.")





    def return_borrowed_book(lib_books: dict, borrower: Borrower):
            print("Select a book to return by entering its index:")
            LibSys.print_books_in_library(lib_books)
            try:
                while True:
                    book_index = Vald.read_in_value(Vald.validate_is_alnum,\
                    message="Enter the index of the book to return (\"X\" to cancel) ->: ")
                    if book_index.lower() == "x":
                        print(f"[i]: Canceling...")
                        break
                    elif book_index.isnumeric():
                        if book_index >= 0 and book_index < len(lib_books):
                            book = list(lib_books.values())[book_index]
                            if book.is_borrowed:
                                # Update book.borrower here if needed
                                print(f"Book '{book.title}' has been returned by {borrower.id}.")
                                LibSys.calculate_funds_collected()
                                borrower.borrowed_books.remove(book)
                                lib_books[book_index](book) #Check functionality
                                
                                weeks_borrowed = int(input('How many weeks ago did you borrow the book?: '))
                                if weeks_borrowed > book.max_weeks_borrow:
                                    LibSys.collect_fine(book, borrower.id)
                                    book.is_borrowed = False
                                    break
                                elif weeks_borrowed < book.max_weeks_borrow:
                                    print(f"The book {book.title} is not overdue. No fines.")
                                else:
                                    print("Invalid")   
                            else:
                                print(f"The book '{book.title}' is not currently borrowed.")
                        else:
                            print("\n[i]: Invalid book index. Please select a valid book.")
                            continue
                    else:
                        print("\n[i]: Invalid input.")
                        continue
            except ValueError:
                print("Invalid input. Please enter a valid book index.")



#############################Check functionality################################

    def collect_fine(book):
        if isinstance(book, LiteraturBook):
            fine = book.fine
            print(f"Ure late, fine : {fine} bring me my money")
        elif isinstance(book, ScienceBook):
            fine = book.fine
            print(f"Ure late, fine : {fine} bring me my money")
        elif isinstance(book, EntertainmentBook):
            fine = book.fine
            print(f"Ure late, fine : {fine} bring me my money")

            return fine
        
    def calculate_funds_collected(lib_books):
            total_student_funds = 0
            total_teacher_funds = 0
            total_fines = 0  

            for book in lib_books.values():
                if isinstance(book, LiteraturBook) or isinstance(book, ScienceBook) or isinstance(book, EntertainmentBook):
                    total_student_funds += book.student_price
                    total_teacher_funds += book.teacher_price
                if book.fine > 0:
                    total_fines += book.fine

            print(f"Total funds collected from students: SEK {total_student_funds}")
            print(f"Total funds collected from teachers: SEK {total_teacher_funds}")
            print(f"Total funds collected from fines: SEK {total_fines}")
            print(f"Total funds collected (including fines): SEK {total_student_funds + total_teacher_funds + total_fines}")


################################################################################


                
    def run():
        while True:
            print(LibSys.show_main_menu())
            user_choice = input("Your choice: ")
            if user_choice == "1":
                LibSys.register_user(user_choice, LibSys.student_db, LibSys.teacher_db)
            elif user_choice == "2":
                LibSys.login_menu(LibSys.student_db, LibSys.teacher_db, LibSys.lib_books, LibSys.id_input)
            elif user_choice == "3":
                LibSys.add_book_to_libary(lib_books=LibSys.lib_books, book_id=LibSys.book_id)
            elif user_choice == "4":
                LibSys.print_books_in_library(lib_books=LibSys.lib_books)
                ###################TODO#######################
                #Current funds collecter
                #How many books are borrowed
                # Maybe as menu?
            elif user_choice == "5":
                print(f"\n[i]: Exiting program...\n")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                