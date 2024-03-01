from address import Address
class Person:
    """ Base class for Administration Teach and Student"""
    def __init__(self,first_name:str,
                 last_name:str,
                 age:int,
                 address:Address, # aggregation or integration
                 mobile_number:str) -> None:
        #validation
        if isinstance(first_name,str) and first_name.strip().isalpha():
            self.first_name = first_name
        else:
            raise ValueError("[i] Bad value First name")
        if isinstance(last_name,str) and last_name.strip().isalpha():
            self.last_name = last_name
        else:
            raise ValueError("[i] Bad value Last name")
        if isinstance(age,int) and 18<=age < 70:
            self.age = age
        else:
            raise ValueError("[i] Bad value age")
        if isinstance(address,Address) :
            self.address = address
        else:
            raise ValueError("[i] Bad value Address")
        if isinstance(mobile_number,str) and mobile_number.strip().isnumeric():
            self.mobile_number = mobile_number
        else:
            raise ValueError("[i] Bad value Mobile number")
    
    def __str__(self) -> str:
        return f"First Name = {self.first_name}\n"+\
                f"Last Name = {self.last_name}\n"+\
                f"Age = {self.age}\n"+\
                f"Address = {self.address.__str__()}"+\
                f"Mobile Number = {self.mobile_number}\n"

##testing##
"""
add_1 = Address(street_name="Blidvädersgatan",
                house_apt_num='8',
                city_name="Tranås",
                zip_code=47337)
person_1 = Person(first_name="Ammar",
                  last_name="Python",
                  age= 41,
                  address=add_1,
                  mobile_number="0700050401")
print(person_1)
"""       