from user import pvt_user
from user import corp_user
from validation import Validations as valid
import os 
import csv



class CSV_OP():
    # Get the path to the current script
    current_script_path = os.path.dirname(os.path.abspath(__file__))

    # Construct file paths relative to the current script
    PVT_DB = os.path.join(current_script_path, "csv_files", "pvt_user.csv")
    CORP_DB = os.path.join(current_script_path, "csv_files", "corp_user.csv")
    ITEM_DB = os.path.join(current_script_path, "csv_files", "items.csv")
    CARD_INFO_DB = os.path.join(current_script_path, "csv_files", "card_info.csv")
    BANK_INFO_DB = os.path.join(current_script_path, "csv_files", "bank_info.csv")
    PAYMENT_INFO_DB = os.path.join(current_script_path, "csv_files", "payment_info.csv")
    VEHICLE_DB = os.path.join(current_script_path, "csv_files", "vehicle_info.csv")
    ORDER_DB = os.path.join(current_script_path, "csv_files", "order_info.csv")
    
    """
    PVT_DB = "exam_2/csv_files/pvt_user.csv"
    CORP_DB = "exam_2/csv_files/corp_user.csv"
    ITEM_DB = "exam_2/csv_files/items.csv"
    CARD_INFO_DB = "exam_2/csv_files/card_info.csv"
    BANK_INFO_DB = "exam_2/csv_files/bank_info.csv"
    PAYMENT_INFO_DB = "exam_2/csv_files/payment_info.csv"
    VEHICLE_DB = "exam_2/csv_files/vehicle_info.csv"
    ORDER_DB = "exam_2/csv_files/order_info.csv"
    """

    def __init__(self):
        self.valid = valid()
    """USER"""
    def user_exists(self, user_id):
        if not os.path.exists(self.PVT_DB):
            return False  # CSV file doesn't exist, so the user can't exist

        with open(self.PVT_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["user_id"] == user_id:
                    return True  # User with the given user_id exists in the CSV

        return False 

    def corp_user_exists(self, corp_id):
        if not os.path.exists(self.CORP_DB):
            return False  # CSV file doesn't exist, so the user can't exist

        with open(self.CORP_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["corp_id"] == corp_id:
                    return True  # User with the given corp_id exists in the CSV

        return False 

    def add_pvt_user(self, user_id, full_name, address, number, email, password):
        user = pvt_user(user_id, full_name, address, number, email, password)

        if self.user_exists(user_id):
            print("User already exists")
            return

        if not os.path.exists(self.PVT_DB):
            with open(self.PVT_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["user_id", "full_name", "address", "number", "email", "password"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        with open(self.PVT_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["user_id", "full_name", "address", "number", "email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            user_data = {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "address": user.address,
                "number": user.number.replace("07", "+46"),
                "email": user.email,
                "password": user.password
            }
            writer.writerow(user_data)
        print("User registration successful")

    def remove_pvt_user(self, user_id):
        if not os.path.exists(self.PVT_DB):
            print("User database does not exist.")
            return

        users = []
        with open(self.PVT_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user_id'] != user_id:
                    users.append(row)

        if len(users) == 0:
            print("User not found.")
            return

        with open(self.PVT_DB, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["user_id", "full_name", "address", "number", "email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for user in users:
                writer.writerow(user)

        print(f"User {user_id} removed successfully.")

    def update_pvt_user(self, user_id, updated_data):
        if not os.path.exists(self.PVT_DB):
            print("User database does not exist.")
            return

        users = []
        with open(self.PVT_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user_id'] == user_id:
                    updated_user = {**row, **updated_data}
                    users.append(updated_user)
                else:
                    users.append(row)
        
        if len(users) == 0:
            print("User not found.")
            return

        with open(self.PVT_DB, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["user_id", "full_name", "address", "number", "email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for user in users:
                writer.writerow(user)

        print(f"User {user_id} updated successfully.")

    def find_pvt_user(self, user_id):
        user_info = None

        if not os.path.exists(self.PVT_DB):
            return user_info  # CSV file doesn't exist, so the user can't exist

        with open(self.PVT_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["user_id"] == user_id:
                    user_info = row  # Store the user info in the user_info variable
                    break

        return user_info  # Return user info if found, None if not found

    def add_corp_user(self, corp_id, company_name, company_address, reference_person_name, reference_person_phone, reference_person_email, invoices_email, password):
        user = corp_user(corp_id, company_name, company_address, reference_person_name, reference_person_phone, reference_person_email, invoices_email, password)

        if self.corp_user_exists(corp_id):
            print("User already exists")
            return

        if not os.path.exists(self.CORP_DB):
            with open(self.CORP_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["corp_id", "company_name", "company_address", "reference_person_name", "reference_person_phone", "reference_person_email", "invoices_email", "password"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        with open(self.CORP_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["corp_id", "company_name", "company_address", "reference_person_name", "reference_person_phone", "reference_person_email", "invoices_email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            user_data = {
                "corp_id": user.corp_id,
                "company_name": user.company_name,
                "company_address": user.company_address,
                "reference_person_name": user.reference_person_name,
                "reference_person_phone": user.reference_person_phone.replace("07", "+46"),
                "reference_person_email": user.reference_person_email,
                "invoices_email":user.invoices_email,
                "password": user.password
            }
            writer.writerow(user_data)
        print("Corporate User registration successful")

    def remove_corp_user(self, corp_id):
        if not os.path.exists(self.CORP_DB):
            print("User database does not exist.")
            return

        users = []
        with open(self.CORP_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['corp_id'] != corp_id:
                    users.append(row)

        if len(users) == 0:
            print("User not found.")
            return

        with open(self.CORP_DB, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["corp_id", "company_name", "company_address", "reference_person_name", "reference_person_phone", "reference_person_email", "invoices_email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for user in users:
                writer.writerow(user)

        print(f"User {corp_id} removed successfully.")

    def update_corp_user(self, corp_id, updated_data):
        if not os.path.exists(self.CORP_DB):
            print("User database does not exist.")
            return

        users = []
        with open(self.CORP_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['corp_id'] == corp_id:
                    # Merge the updated data with the existing data, but only if updated_data is not None
                    updated_user = {key: updated_data[key] if updated_data[key] is not None else row[key] for key in row}
                    users.append(updated_user)
                else:
                    users.append(row)

        if len(users) == 0:
            print("User not found.")
            return

        with open(self.CORP_DB, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["corp_id", "company_name", "company_address", "reference_person_name", "reference_person_phone", "reference_person_email", "invoices_email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for user in users:
                writer.writerow(user)

        print(f"User {corp_id} updated successfully.")
    
    def find_corp_user(self,corp_id):
        user_info = None

        if not os.path.exists(self.CORP_DB):
            return user_info  # CSV file doesn't exist, so the user can't exist

        with open(self.CORP_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["corp_id"] == corp_id:
                    user_info = row  # Store the user info in the user_info variable
                    break

        return user_info  # Return user info if found, None if not found

    """ITEMS"""
    def create_items(self,):
         # Define the items
        items = [
        {"name": "Smartphone", "price_per_kg": 299.99, "volume": 0.2, "weight": 0.15, "item_type": "fragile", "shop_name": "ElectronicsRUs"},
        {"name": "Laptop", "price_per_kg": 799.99, "volume": 0.5, "weight": 2.0, "item_type": "solid", "shop_name": "Tech Haven"},
        {"name": "Coffee Maker", "price_per_kg": 49.99, "volume": 0.3, "weight": 2.5, "item_type": "solid", "shop_name": "Kitchen Essentials"},
        {"name": "Glass Vase", "price_per_kg": 29.99, "volume": 0.1, "weight": 0.5, "item_type": "fragile", "shop_name": "Home Decor Plus"},
        {"name": "Toaster", "price_per_kg": 34.99, "volume": 0.2, "weight": 1.0, "item_type": "solid", "shop_name": "Kitchenware Hub"},
        {"name": "Television", "price_per_kg": 599.99, "volume": 0.8, "weight": 8.0, "item_type": "solid", "shop_name": "ElectronicsRUs"},
        {"name": "Porcelain Plate", "price_per_kg": 14.99, "volume": 0.05, "weight": 0.2, "item_type": "fragile", "shop_name": "Home Decor Plus"},
        {"name": "Desk Chair", "price_per_kg": 74.99, "volume": 0.3, "weight": 4.0, "item_type": "solid", "shop_name": "Furniture Emporium"},
        {"name": "Ceramic Mug", "price_per_kg": 7.99, "volume": 0.01, "weight": 0.2, "item_type": "fragile", "shop_name": "Kitchenware Hub"},
        {"name": "Washing Machine", "price_per_kg": 299.99, "volume": 1.0, "weight": 50.0, "item_type": "solid", "shop_name": "Appliance Central"},
        {"name": "Wall Clock", "price_per_kg": 19.99, "volume": 0.02, "weight": 0.5, "item_type": "fragile", "shop_name": "Home Decor Plus"},
        {"name": "Refrigerator", "price_per_kg": 499.99, "volume": 1.5, "weight": 70.0, "item_type": "solid", "shop_name": "Appliance Central"},
        {"name": "Crystal Vase", "price_per_kg": 39.99, "volume": 0.1, "weight": 0.4, "item_type": "fragile", "shop_name": "Home Decor Plus"},
        {"name": "Coffee Table", "price_per_kg": 49.99, "volume": 0.4, "weight": 10.0, "item_type": "solid", "shop_name": "Furniture Emporium"},
        {"name": "Ceramic Plate", "price_per_kg": 11.99, "volume": 0.05, "weight": 0.3, "item_type": "fragile", "shop_name": "Kitchenware Hub"},
        {"name": "Microwave", "price_per_kg": 79.99, "volume": 0.2, "weight": 12.0, "item_type": "solid", "shop_name": "Appliance Central"},
        {"name": "Glass Tumbler", "price_per_kg": 3.99, "volume": 0.02, "weight": 0.2, "item_type": "fragile", "shop_name": "Kitchenware Hub"},
        {"name": "Computer Monitor", "price_per_kg": 129.99, "volume": 0.05, "weight": 7.0, "item_type": "solid", "shop_name": "Tech Haven"},
        {"name": "Porcelain Teapot", "price_per_kg": 19.99, "volume": 0.05, "weight": 0.6, "item_type": "fragile", "shop_name": "Kitchenware Hub"},
        {"name": "Bookshelf", "price_per_kg": 59.99, "volume": 0.3, "weight": 15.0, "item_type": "solid", "shop_name": "Furniture Emporium"},
        {"name": "Glass Bowl", "price_per_kg": 8.99, "volume": 0.01, "weight": 0.3, "item_type": "fragile", "shop_name": "Kitchenware Hub"},
        {"name": "DVD Player", "price_per_kg": 39.99, "volume": 0.02, "weight": 2.0, "item_type": "solid", "shop_name": "ElectronicsRUs"},
        {"name": "Porcelain Figurine", "price_per_kg": 9.99, "volume": 0.02, "weight": 0.1, "item_type": "fragile", "shop_name": "Home Decor Plus"},
        {"name": "Sofa", "price_per_kg": 199.99, "volume": 1.0, "weight": 30.0, "item_type": "solid", "shop_name": "Furniture Emporium"},
    ]

         # Check if the items CSV file exists, and create it with a header row if not
        if not os.path.exists(self.ITEM_DB):
            with open(self.ITEM_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["name", "price_per_kg", "volume", "weight", "item_type", "shop_name"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        # Write the item data to the CSV file
        with open(self.ITEM_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "price_per_kg", "volume", "weight", "item_type", "shop_name"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            for item in items:
                writer.writerow(item)

        print(f"Items data has been written to '{self.ITEM_DB}'.")

    def get_items(self):
        
        items = []
        try:
            with open(self.ITEM_DB, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    items.append({
                        "name": row["name"],
                        "price_per_kg": float(row["price_per_kg"]),
                        "volume": float(row["volume"]),
                        "weight": float(row["weight"]),
                        "item_type": row["item_type"],
                        "shop_name": row["shop_name"]
                    })
        except FileNotFoundError:
            print(f"File 'self.ITEM_DB' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

        return items

    """VEHICLES""" 
    def create_vehicles(self, vehicle_data):
        # Check if the vehicles CSV file exists, and create it with a header row if not
        if not os.path.exists(self.VEHICLE_DB):
            with open(self.VEHICLE_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["id", "name", "max_capacity_kg", "max_capacity_items", "location", "type", "status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        # Write the vehicle data to the CSV file
        with open(self.VEHICLE_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["id", "name", "max_capacity_kg", "max_capacity_items", "location", "type", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writerow(vehicle_data)

    def vehicle_exists(self,id):
        if not os.path.exists(self.VEHICLE_DB):
            return False  # CSV file doesn't exist, so the user can't exist

        with open(self.VEHICLE_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["id"] == id:
                    return True  # User with the given user_id exists in the CSV

        return False 

    def find_vehicle(self, id):
        vehicle_info = None

        if not os.path.exists(self.VEHICLE_DB):
            return vehicle_info  # CSV file doesn't exist, so the vehicle can't be found

        with open(self.VEHICLE_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["id"] == id:
                    vehicle_info = row  # Store the vehicle info in the vehicle_info variable
                    break

        return vehicle_info  # Return vehicle info if found, None if not found

    def get_vehicles(self):
        vehicles = []
        try:
            with open(self.VEHICLE_DB, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    vehicles.append({
                        "id": row["id"],
                        "name": row["name"],
                        "max_capacity_kg": float(row["max_capacity_kg"]),
                        "max_capacity_items": int(row["max_capacity_items"]),
                        "location": row["location"],
                        "type": row["type"],
                        "status": row["status"]
                    })
        except FileNotFoundError:
            print(f"File '{self.VEHICLE_DB}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

        return vehicles

    def select_vehicle(self, total_weight, total_items):
            available_vehicles = self.get_vehicles()

            # Filter vehicles based on maximum capacity
            suitable_vehicles = [vehicle for vehicle in available_vehicles if
                                vehicle["max_capacity_kg"] >= total_weight and
                                vehicle["max_capacity_items"] >= total_items]

            if not suitable_vehicles:
                print("No suitable vehicles available for the shipment.")
                return None

            # Calculate excess capacity for each suitable vehicle
            for vehicle in suitable_vehicles:
                excess_weight = vehicle["max_capacity_kg"] - total_weight
                excess_items = vehicle["max_capacity_items"] - total_items
                vehicle["excess_capacity"] = excess_weight + excess_items

            # Sort vehicles by excess capacity in ascending order
            suitable_vehicles.sort(key=lambda vehicle: vehicle["excess_capacity"])

            # Choose the vehicle with the least excess capacity (i.e., the best fit)
            best_vehicle = suitable_vehicles[0]

            return best_vehicle
        
    """PAYMENTS"""
    def add_card_info(self, name, card_number, card_holder):
         # Check if the card info CSV file exists, and create it with a header row if not
        if not os.path.exists(self.CARD_INFO_DB):
            with open(self.CARD_INFO_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["user_id", "card_number", "card_holder"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        card_info = {
            "user_id": name,
            "card_number": card_number,
            "card_holder": card_holder
        }

        # Append the card information to the CSV file
        with open(self.CARD_INFO_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["user_id", "card_number", "card_holder"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writerow(card_info)

        print("Card information added successfully.")
    
    def add_bank_info(self, name, account_number, account_holder_name):

        # Check if the bank info CSV file exists, and create it with a header row if not
        if not os.path.exists(self.BANK_INFO_DB):
            with open(self.BANK_INFO_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["user_id", "account_number", "account_holder_name"]  # Header row
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        bank_info = {
            "user_id": name,
            "account_number": account_number,
            "account_holder_name": account_holder_name
        }

        # Append the bank information to the CSV file
        with open(self.BANK_INFO_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["user_id", "account_number", "account_holder_name"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writerow(bank_info)

        print("Bank information added successfully.")

    def add_payment_info(self, transaction_id, user_id, amount, payment_method, payment_status):
    # Check if the payment info CSV file exists, and create it with a header row if not
        if not os.path.exists(self.PAYMENT_INFO_DB):
            with open(self.PAYMENT_INFO_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["transaction_id", "user_id", "amount", "payment_method", "payment_status"]  # Header row
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        payment_info = {
            "transaction_id": transaction_id,
            "user_id": user_id,
            "amount": amount,
            "payment_method": payment_method,
            "payment_status": payment_status
        }

        # Append the payment information to the CSV file
        with open(self.PAYMENT_INFO_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["transaction_id", "user_id", "amount", "payment_method", "payment_status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writerow(payment_info)

        print("Payment information added successfully.")
    
    """ORDERS"""
    def add_order(self, order_id, order_priority, sender, to_location, items, payment_details, total_weight, order_status, vehicle, total_price):
        

        order_data = {
            "order_id": order_id,
            "order_priority": order_priority,
            "sender": sender,
            "to_location": to_location,
            "items": items,
            "payment_details": payment_details,
            "total_weight": total_weight,
            "order_status": order_status,
            "vehicle": vehicle,
            "total_price": total_price
        }

        # Check if the orders CSV file exists, and create it with a header row if not
        if not os.path.exists(self.ORDER_DB):
            with open(self.ORDER_DB, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["order_id","order_priority", "sender", "to_location", "items", "payment_details", "total_weight","total_price", "order_status", "vehicle"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                writer.writeheader()

        # Write the order data to the CSV file
        with open(self.ORDER_DB, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["order_id","order_priority", "sender", "to_location", "items", "payment_details", "total_weight", "total_price", "order_status", "vehicle"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
            writer.writerow(order_data)

        print("Order has been added to the CSV file.")

    def get_customer(self, user_id):
        user_info = None

        if not os.path.exists(self.PVT_DB):
            return user_info  # CSV file doesn't exist, so the user can't exist

        # Search for the user in the private user database (PVT_DB)
        with open(self.PVT_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["user_id"] == user_id:
                    user_info = row  # Store the user info in the user_info variable
                    break

        if user_info is None and os.path.exists(self.CORP_DB):
            # If user was not found in the private user database, search in the corporate user database (CORP_DB)
            with open(self.CORP_DB, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["corp_id"] == user_id:
                        user_info = row  # Store the user info in the user_info variable
                        break

        return user_info  # Return user info if found, None if not found

    def get_order(self, order_id):
        order_info = None

        if not os.path.exists(self.ORDER_DB):
            return order_info  # CSV file doesn't exist, so the order can't exist

        # Search for the order in the order database (ORDER_DB)
        with open(self.ORDER_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["order_id"] == order_id:
                    order_info = row  # Store the order info in the order_info variable
                    break

        return order_info

    def update_order_status(self, order_id, new_status):
            if not os.path.exists(self.ORDER_DB):
                return None  # CSV file doesn't exist, so the order can't exist

            updated_status = []  # Initialize a list to store updated order records

            with open(self.ORDER_DB, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["order_id"] == order_id:
                        # Update the order_status field with the new status
                        row["order_status"] = new_status
                    updated_status.append(row)  # Append the updated row to the list

            # Write the updated order information back to the CSV file
            with open(self.ORDER_DB, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_status)

            return updated_status

    def update_order(self, order_id, new_items, total_weight, total_price):
        if not os.path.exists(self.ORDER_DB):
            return None  # CSV file doesn't exist, so the order can't exist

        # Search for the order in the order database (ORDER_DB)
        updated_orders = [] 

        with open(self.ORDER_DB, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["order_id"] == order_id:
                    # Get the current items, if any, and split them into a list
                    current_items = row["items"].split(", ") if row["items"] else []
                    # Split the new items string into a list
                    new_items = new_items.split(", ")
                    # Append the new items to the current items
                    updated_items = current_items + new_items
                    # Join the updated items back into a single string
                    row["items"] = ", ".join(updated_items)
                    # Update total weight and total price
                    row["total_weight"] = total_weight
                    row["total_price"] = total_price
                updated_orders.append(row)

        # Write the updated order information back to the CSV file
        with open(self.ORDER_DB, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = updated_orders[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_orders)

        return updated_orders








"""
# Vehicle Test

# Create an instance of the CSV_OP class
csv_operator = CSV_OP()

# Shipment 1: 1 item and total weight 5kg
total_weight_1 = 5.0
total_items_1 = 1
best_vehicle_1 = csv_operator.select_vehicle(total_weight_1, total_items_1)
if best_vehicle_1:
    print(f"Shipment 1: The best vehicle for the shipment has ID: {best_vehicle_1['id']}")
else:
    print("Shipment 1: No suitable vehicles available for the shipment.")

# Shipment 2: 12 items and total weight 3kg
total_weight_2 = 3.0
total_items_2 = 12
best_vehicle_2 = csv_operator.select_vehicle(total_weight_2, total_items_2)
if best_vehicle_2:
    print(f"Shipment 2: The best vehicle for the shipment has ID: {best_vehicle_2['id']}")
else:
    print("Shipment 2: No suitable vehicles available for the shipment.")

# Shipment 3: 60 items and total weight 4500kg
total_weight_3 = 4500.0
total_items_3 = 60
best_vehicle_3 = csv_operator.select_vehicle(total_weight_3, total_items_3)
if best_vehicle_3:
    print(f"Shipment 3: The best vehicle for the shipment has ID: {best_vehicle_3['id']}")
else:
    print("Shipment 3: No suitable vehicles available for the shipment.")

# Shipment 4: 120 items and total weight 2500kg
total_weight_4 = 2500.0
total_items_4 = 120
best_vehicle_4 = csv_operator.select_vehicle(total_weight_4, total_items_4)
if best_vehicle_4:
    print(f"Shipment 4: The best vehicle for the shipment has ID: {best_vehicle_4['id']}")
else:
    print("Shipment 4: No suitable vehicles available for the shipment.")
    """