from address import Address
from person import Person
class Administration(Person):
    def __init__(self, first_name: str, last_name: str,\
                age: int, address: Address, mobile_number: str) -> None:
        super().__init__(first_name, last_name, age, address, mobile_number)
    
    def __str__(self) -> str:
        return "I'm admin\n"+super().__str__()

##Testing##
"""
add_1 = Address(street_name="Blidvädersgatan",
                house_apt_num='8',
                city_name="Tranås",
                zip_code=47337)
admin_1 = Administration(first_name="AmmarAdmin",
                  last_name="Python",
                  age= 41,
                  address=add_1,
                  mobile_number="0700050401")
#print(admin_1)
print(f" admin is Person = {isinstance(admin_1,Person)}")
print(f" admin is Administration = {isinstance(admin_1,Administration)}")

"""