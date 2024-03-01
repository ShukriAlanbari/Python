
from address import Address
from person import Person

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str,\
                  age: int, address: Address,
                  mobile_number: str) -> None:
        super().__init__(first_name, last_name, age, address, mobile_number)
    
    def __str__(self) -> str:
        return "I'm a Teacher\n"+super().__str__()

"""
##testing##

add_1 = Address(street_name="Blidvädersgatan",
                house_apt_num='8',
                city_name="Tranås",
                zip_code=47337)
teacher_1 = Teacher(first_name="AmmarTeacher",
                  last_name="Python",
                  age= 41,
                  address=add_1,
                  mobile_number="0700050401")
print(teacher_1)
"""   