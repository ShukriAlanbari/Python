"""
group_name:
teacher(s)
student(s)

Method : 
1- Add students to teacher as student group.
    we need to create student_group 
    as an object
    --> (OOP).

5- Print student group belong to the teacher.
"""
from student import Student
from teacher import Teacher
class StudyGroup:
    def __init__(self, study_group_name:str) -> None:
        if isinstance(study_group_name,str):
            self.study_group_name = study_group_name
        else:
            raise ValueError("[i] Bad Value study group name")
        self.students = list()
        self.teachers = list()
    
    def add_a_student(self,student:Student):
        if isinstance(student,Student):
            if student not in self.students:
                self.students.append(student)
                return True
            else:
                raise ValueError("[ii] Student already existed")
            
        else:
            raise ValueError("[i] Bad value student")
    
    def add_a_teacher(self,teacher:Teacher):
        if isinstance(teacher,Teacher):
            if teacher not in self.teachers:
                self.teachers.append(teacher)
                return True
            else:
                raise ValueError("[ii] Student already existed")
            
        else:
            raise ValueError("[i] Bad value student")
    
    def print_group_to_teacher(self,teacher:Teacher) -> str:
        if isinstance(teacher,Teacher):
            if teacher in self.teachers:
                return "".join([student.__str__()+"\n"  for student in self.students]) 
                
            else:
                return None
            
        else:
            raise ValueError("[i] Bad value student")
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
study_group_1 = StudyGroup(study_group_name="Pythonic Group")
teacher_1 = Teacher(first_name="AmmarTeacher",
                  last_name="Python",
                  age= 41,
                  address=add_1,
                  mobile_number="0700050401")
if study_group_1.add_a_student(student=student_1) and \
    study_group_1.add_a_student(student=student_2) and \
        study_group_1.add_a_teacher(teacher=teacher_1):
        print(study_group_1.print_group_to_teacher(teacher=teacher_1))
"""