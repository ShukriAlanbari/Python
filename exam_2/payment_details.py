import uuid
from validation import Validations as valid

class Payment:
    def __init__(self, payment_method, amount, payment_status, card_number=None, card_holder_name=None, account_number=None, account_holder_name=None):
        self.payment_method = payment_method
        self.transaction_id = self.generate_transaction_id()
        self.amount = amount
        self.payment_status = payment_status
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.account_number = account_number
        self.account_holder_name = account_holder_name





    
    def generate_transaction_id():
        return str(uuid.uuid4())
    
    