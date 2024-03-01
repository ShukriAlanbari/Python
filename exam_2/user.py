from validation import Validations as valid

class pvt_user:
    def __init__(self, user_id, full_name, address, number, email, password):
        self.user_id = None
        self.full_name = None
        self.address = None
        self.number = None
        self.email = None
        self.password = None

        if valid.valid_id(user_id):
            self.user_id = user_id
        else:
            raise ValueError(f"[!] Invalid Id: {user_id}")

        if valid.valid_name(full_name):
            self.full_name = full_name
        else:
            raise ValueError(f"[!] Invalid Name: {full_name}")

        if valid.valid_address(address):
            self.address = address
        else:
            raise ValueError(f"[!] Invalid Address: {address}")

        if valid.valid_phone(number):
            self.number = number
        else:
            raise ValueError(f"[!] Invalid Phone number: {number}")

        if valid.valid_email(email):
            self.email = email
        else:
            raise ValueError(f"[!] Invalid Email: {email}")

        if valid.valid_password(password):
            self.password = password
        else:
            raise ValueError(f"[!] Invalid Password: {password}")




class corp_user:
   
    def __init__(self,corp_id, company_name, company_address, reference_person_name, reference_person_phone, reference_person_email, invoices_email, password):
        self.corp_id = None
        self.company_name = None
        self.company_address = None
        self.reference_person_name=None
        self.reference_person_phone = None
        self.reference_person_email = None
        self.invoices_email = None
        self.password= None

        if valid.valid_id(corp_id):
                self.corp_id = corp_id
        else:
                raise ValueError(f"[!] Invalid ID {corp_id}")
            
        if valid.valid_company_name(company_name):
                self.company_name = company_name
        else:
                raise ValueError(f"[!] Invalid company name {company_name}")
            
        if valid.valid_address(company_address):
                self.company_address = company_address
        else:
                raise ValueError(f"[!] Invalid company address {company_address}")
            
        if valid.valid_name(reference_person_name):
                self.reference_person_name = reference_person_name
        else:
                raise ValueError(f"[!] Invalid reference person name {reference_person_name}")
            
        if valid.valid_phone(reference_person_phone):
                self.reference_person_phone = reference_person_phone
        else:
                raise ValueError(f"[!] Invalid reference person phone {reference_person_phone}")
            
        if valid.valid_email(reference_person_email):
                self.reference_person_email = reference_person_email
        else:
                raise ValueError(f"[!] Invalid reference person email {reference_person_email}")
            
        if valid.valid_email(invoices_email):
                self.invoices_email = invoices_email
        else:
                raise ValueError(f"[!] Invalid invoices email {invoices_email}")
        if valid.valid_password(password):
                self.password = password
        else:
                raise ValueError(f"[!] Invalid Password: {password}")
            
