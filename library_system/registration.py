from borrower import Borrower, Teacher, Student
from validations import Validation as Vald
import random

teachers_db = {}
student_db = {}

PROMPT_MENU = '''
Welcome to the Libary, choose one of these options: 

[1] Register New User 
[2] LOGIN as Student 
[3] LOGIN as Teacher 
[4] Add new book to library
[5] Print out all books
[6] ????
[7] Profit
[8] Exit
'''
def show_menu():
    print(PROMPT_MENU)
    
def register_user(choice:int):
    while True:
        try:
            print("Choose one of the options below!\n"
                "\n1- Register a new Student.\n"
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
                mobile_number = Vald.read_in_value(Vald.validate_str_num, 
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
                    input("\nPress enter to go back to start: ")
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
                    input("\nPress enter to go back to start: ")
                    break
                
            elif choice == 3:
                break
            else:
                print("[i] You need to choose an alternative from the list.")
                continue
        except ValueError:
            print("[i] Please enter a valid integer choice.")
        
def login_student():
    while True:
        student_id = input("Enter your Student ID (x): ")
        if student_id in student_db:
            print("\nLogin successful!\n")
            print("Student Information:\n")
            print(student_db[student_id])
            print("Choose one of the options below!\n"
                "\n1- Borrow a new book.\n"
                "2- Return a book.\n"
                "3- Logout.\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Print out library book_list
                pass
            elif choice == 2:
                # Print your book_list
                pass
            elif choice == 3:
                break
            else:
                print("[i] You need to choose an alternative from the list.")
        elif student_id.lower() == "x":
            break
        else:
            print("Student not found. Please check your ID.")
            continue
        
def login_teacher():
    while True:
        teacher_id = input("Enter your Teacher ID(x to go back): ")
        if teacher_id in teacher_db:
            print("\nLogin successful!\n")
            print("Teacher Information:")
            print(teacher_db[teacher_id])
            logout = input("Logout from account enter (x): ")
            if logout.lower() == "x":
                break
        elif teacher_id.lower() == "x":
            break
        else:
            print("Teacher not found. Please check your ID.")
            continue
        
def run():
    while True:
        show_menu()
        user_choice = input("Your choice: ")
        
        if user_choice == "1":
            register_user(user_choice)
        elif user_choice == "2":
            login_student()
        elif user_choice == "3":
            login_teacher()
        elif user_choice == "4":
            pass
        elif user_choice == "5":
            pass
        elif user_choice == "6":
            pass
        elif user_choice == "7":
            pass
        elif user_choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    student_db = dict()
    teacher_db = dict()
    run()