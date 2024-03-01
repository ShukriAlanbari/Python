
from student import Student
class ClassRoom:
    def __init__(self,class_room_name:str,class_room_number:int) -> None:
        if isinstance(class_room_name,str):
            self.class_room_name = class_room_name
        else:
            raise ValueError("[i] Bad Value classroom name ")
        if isinstance(class_room_number,int):
            self.class_room_number = class_room_number
        else:
            raise ValueError("[i] Bad Value classroom number")
        self.students = list()
    
    def add_a_student(self,student:Student):
        if isinstance(student,Student):
            if student not in self.students:
                self.students.append(student)
                return True
            else:
                raise ValueError("[ii] Student already existed")
            
        else:
            raise ValueError("[i] Bad value student")
    
    def print_student_list(self)-> str :
        return "".join([student.__str__()+"\n"  for student in self.students]) 

"""
##testing##
from address import Address
add_1 = Address(street_name="Blidvädersgatan",
                house_apt_num='8',
                city_name="Tranås",
                zip_code=47337)
student_1 = Student(first_name="AmmarStudent",
                  last_name="Python",
                  age= 41,
                  address=add_1,
                  mobile_number="0700050401")
student_2 = Student(first_name="AmmarBrother",
                  last_name="Python",
                  age= 37,
                  address=add_1,
                  mobile_number="0700060401")
classroom_1 = ClassRoom(class_room_name="THS",class_room_number=1)
if classroom_1.add_a_student(student=student_1) and \
    classroom_1.add_a_student(student=student_2):
        print(classroom_1.print_student_list())
"""