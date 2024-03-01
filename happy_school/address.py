class Address:
    """Address is class to create address objects """

    # constructor
    def __init__(self,street_name:str,
                 house_apt_num:str,
                 city_name:str,
                 zip_code:int) -> None:
        # validation
        if isinstance(street_name,str) and street_name.strip().isalpha():
            self.street_name = street_name
        else:
            raise ValueError("[i] Bad value street name")
        if isinstance(house_apt_num,str) and house_apt_num.strip().isalnum():
            self.house_apt_num = house_apt_num
        else:
            raise ValueError("[i] Bad value house or apartment number ")
        if isinstance(city_name,str) and city_name.strip().isalpha():
            self.city_name = city_name
        else:
            raise ValueError("[i] Bad value city name ")
        if isinstance(zip_code,int) :
            self.zip_code = zip_code
        else:
            raise ValueError("[i] Bad value zip code ")

    # __str__
    def __str__(self) -> str:
        return f"Street Name = {self.street_name}\n"+\
                f"House or apartment number = {self.house_apt_num}\n"+\
                f"City = {self.city_name}\n"+\
                f"Zip_Code = {self.zip_code}\n"
    
##testing##

"""
add_1 = Address(street_name="Blidvädersgatan",
                house_apt_num='8',
                city_name="Tranås",
                zip_code=47337)
print(add_1)
"""
