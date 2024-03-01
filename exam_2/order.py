import uuid
import random
import string
from datetime import datetime
from user import pvt_user, corp_user
from payment_details import Payment
from validation import Validations as valid
import csv
class Order:
    def __init__(self, order_id, order_priority, sender, customer, to_location, items,  payment_details, total_weight, order_status, vehicle, total_price):
        self.order_id = order_id
        self.order_priority = order_priority
        self.sender = sender
        self.to_location = to_location
        self.payment_details = payment_details
        self.items = []
        self.total_weight = total_weight
        self.order_status = order_status
        self.order_place_datetime = datetime.now()
        self.order_delivery_datetime = None
        self.vehicle = vehicle
        self.customer= customer
        self.total_price= total_price




    def generate_order_id():
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        numbers = ''.join(random.choice(string.digits) for _ in range(5))
        return f"{letters}{numbers}"
    

    def add_item_to_basket(self, item):
        # Extract and store only the name and price of the item
        item_info = {
            "name": item["name"],
            "price_per_kg": item["price_per_kg"],
            "shop_name": item["shop_name"],
            "weight": item["weight"]
        }
        self.items.append(item_info)

    def get_basket(self):
        # Return the list of selected items
        return self.items

    def get_sender_info(self):
        sender_info = [f"{item['name']} : {item['shop_name']}" for item in self.items]
        return sender_info

    def delivery_address(self, address):
        self.to_location = address

    def get_payment_details(self, user_id):
        # Create an empty list to store payment details
        payment_details = []

        # Open the payment_info.csv file and read its contents
        with open("exam_2/csv_files/payment_info.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user_id'] == user_id:
                    payment_details.append({
                        'transaction_id': row['transaction_id'],
                        'user_id': row['user_id'],
                        'amount': float(row['amount']),
                        'payment_method': row['payment_method'],
                        'payment_status': row['payment_status']
                    })

        return payment_details

    def calculate_total_weight(self):
    # Calculate the total weight of items in the basket
        total = sum(item["weight"] for item in self.items)
        return total

    def get_order_status(self):
        payment_result = self.process_payment()
        
        if payment_result == "Payment successful":
            self.order_status = "Shipping"
        else:
            self.order_status = "Pending"

    
