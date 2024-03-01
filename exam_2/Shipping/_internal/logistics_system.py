import os
from csv_op import CSV_OP
from validation import Validations as valid
from user import pvt_user
from user import corp_user
from order import Order
from vehicle import Vehicle
from payment_details import Payment


class AdminMenu:

    def main_menu(self):
        ADMINMENU = \
        '''
Logistics System - Admin Menu

1. Add/Remove/Update/Search PVt-Users
2. Add/Remove/Update/Search Corporate-Users
3. Vehicles
4. Orders
5. Choose Vehicle for Shipment and Test
6. Exit
        '''
        print(ADMINMENU)

    def run(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice (1-6): ")
            os.system("cls")
            
            # Add/Remove/Update/Search PVt-Users
            if choice == '1':
                # Submenu for private user management
                while True:
                    print("Private User Management Menu")
                    print("1. Add Private User")
                    print("2. Remove Private User")
                    print("3. Update Private User")
                    print("4. Search private user")
                    print("5. Back to Main Menu")
                    sub_choice = input("Enter your choice (1-5): ")
                    os.system("cls")
                    csv_operator = CSV_OP()
                         
                    # Add a private user
                    if sub_choice == '1':
                        try:
                            while True:  # Keep prompting until valid input
                                user_id = input("Enter user ID (10-Digits): ")
                                if valid.valid_id(user_id):
                                    if not csv_operator.user_exists(user_id):  # Check if the user doesn't exist
                                        break  # Exit the loop when input is valid and the user doesn't exist
                                    else:
                                        print(f"[!] User with ID {user_id} already exists. Please enter a different ID.")
                                else:
                                    print(f"[!] Invalid Id (ex: 9313061312): {user_id}")                           
                             
                            while True:  # Keep prompting until valid input
                                full_name = input("Enter full name (firstName LastName): ")
                                if valid.valid_name(full_name):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Name (John Smith): {full_name}")

                            while True:  # Keep prompting until valid input
                                address = input("Enter address (StreetName BuildingNumber PostNumber City ): ")
                                if valid.valid_address(address):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Address (ex:lindängsvägen 21 52320 Götebörg ): {address}")

                            while True:  # Keep prompting until valid input
                                number = input("Enter phone number (10-digits must start with 07): ")
                                if valid.valid_phone(number):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Phone number (ex: 0712121212): {number}")

                            while True:  # Keep prompting until valid input
                                email = input("Enter email (ex: info@gmail.com): ")
                                if valid.valid_email(email):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {email}")

                            while True:  # Keep prompting until valid input
                                password = input("Enter password (Atleast 1 capital letter and one special character): ")
                                if valid.valid_password(password):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Password (ex: K.aaa): {password}")
                            
                            new_user = pvt_user(user_id, full_name, address, number, email, password)
                            # Create an instance of the CSV_OP class
                            csv_operator = CSV_OP()
                            # Use the CSV_OP class to save user information to a CSV file
                            csv_operator.add_pvt_user(new_user.user_id, new_user.full_name, new_user.address,new_user.number,new_user.email, new_user.password)
                            os.system("cls")
                            print("User registration successful")
                        except Exception as e:
                            print(e)
                            break

                    # Remove a private user                           
                    elif sub_choice == '2':
                        
                        user_id = input("Enter user ID to remove (10-Digits): ")
                        if csv_operator.user_exists(user_id):
                            csv_operator.remove_pvt_user(user_id)
                        else:
                            print(f"user >{user_id}< does not exist.")

                    # Update a private user
                    elif sub_choice == '3':
                        
                        user_id = input("Enter user ID to update (10-Digits): ")
                        if csv_operator.user_exists(user_id):
                            updated_data = {
                                "full_name": None,
                                "address": None,
                                "number": None,
                                "email": None,
                                "password": None
                            }

                            while True:  # Keep prompting until valid input
                                full_name = input("Enter updated full name (firstName LastName): ")
                                if valid.valid_name(full_name):
                                    updated_data["full_name"] = full_name
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Name (ex: John Smith) {full_name}")

                            while True:  # Keep prompting until valid input
                                address = input("Enter updated address(StreetName BuildingNumber PostNumber City ): ")
                                if valid.valid_address(address):
                                    updated_data["address"] = address
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Address(ex:lindängsvägen 21 52320 Götebörg ): {address}")

                            while True:  # Keep prompting until valid input
                                number = input("Enter updated phone number (10-digits must start with 07): ")
                                if valid.valid_phone(number):
                                    updated_data["number"] = number
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Phone number (ex: 0712121212): {number}")

                            while True:  # Keep prompting until valid input
                                email = input("Enter updated email (ex: info@gmail.com): ")
                                if valid.valid_email(email):
                                    updated_data["email"] = email
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {email}")

                            while True:  # Keep prompting until valid input
                                password = input("Enter updated password (Atleast 1 capital letter and one special character): ")
                                if valid.valid_password(password):
                                    updated_data["password"] = password
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Password (ex: K.aaa): {password}")

                            csv_operator.update_pvt_user(user_id, updated_data)
                            os.system("cls")
                            print(f"User {user_id} updated successfully.")
                        else:
                            print(f"user >{user_id}< does not exist.")

                    # Search private users
                    elif sub_choice == "4":
                        user_id = input("Enter user ID (10-Digits): ")
                        user_info = csv_operator.find_pvt_user(user_id)
                        
                        if user_info:
                            # User exists, print out the user info
                            print(f"User Info:\n{user_info}\n")
                        else:
                            print(f"user >{user_id}< does not exist.")
                        
                    # Return to the main menu
                    elif sub_choice == '5':
                       break

                    else:
                        print("Invalid choice. Please select a valid option (1-4) in the sub-menu.")

            # Add/Remove/Update/Search Corporate-Users
            elif choice == '2':
                # Submenu for corporate user management
                while True:
                    print("Corporate User Management Menu")
                    print("1. Add Corporate User")
                    print("2. Remove Corporate User")
                    print("3. Update Corporate User")
                    print("4. Search corporate users")
                    print("5. Back to Main Menu")
                    sub_choice = input("Enter your choice (1-4): ")
                    csv_operator = CSV_OP()

                    # Add a Corporate user
                    if sub_choice == '1':
                         
                        try:
                            while True:  # Keep prompting until valid input
                                corp_id = input("Enter user ID (10-Digits): ")
                                if valid.valid_id(corp_id):
                                    if not csv_operator.corp_user_exists(corp_id):  # Check if the user doesn't exist
                                        break  # Exit the loop when input is valid and the user doesn't exist
                                    else:
                                        print(f"[!] User with ID {corp_id} already exists. Please enter a different ID.")
                                else:
                                    print(f"[!] Invalid Id (ex: 9313061312): {user_id}")                           
                             
                            while True:  # Keep prompting until valid input
                                company_name = input("Enter company name: ")
                                if valid.valid_company_name(company_name):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Name: {company_name}")

                            while True:  # Keep prompting until valid input
                                company_address = input("Enter address (StreetName BuildingNumber PostNumber City ): ")
                                if valid.valid_address(company_address):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Address (ex:lindängsvägen 21 52320 Götebörg ): {address}")
                            
                           
                            while True:
                                reference_person_name= input("Enter reference person full name (firstName LastName): ")
                                if valid.valid_name(reference_person_name):
                                    break
                                else:
                                    print(f"[!] Invalid Name (John Smith): {reference_person_name}")

                            while True:  # Keep prompting until valid input
                                reference_person_phone = input("Enter reference person phone number (10-digits must start with 07):")
                                if valid.valid_phone(reference_person_phone):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Phone number (ex: 0712121212): {reference_person_phone}")

                            while True:  # Keep prompting until valid input
                                reference_person_email = input("Enter reference person email (ex: info@gmail.com): ")
                                if valid.valid_email(reference_person_email):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {reference_person_email}")

                            while True:  # Keep prompting until valid input
                                invoices_email = input("Enter invoices email (ex: info@gmail.com): ")
                                if valid.valid_email(invoices_email):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {invoices_email}")

                            while True:  # Keep prompting until valid input
                                password = input("Enter password (Atleast 1 capital letter and one special character): ")
                                if valid.valid_password(password):
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Password (ex: K.aaa): {password}")
                            
                            new_user = corp_user(corp_id, company_name, company_address, reference_person_name, reference_person_phone, reference_person_email, invoices_email, password)
                            # Create an instance of the CSV_OP class
                            csv_operator = CSV_OP()
                            # Use the CSV_OP class to save user information to a CSV file
                            csv_operator.add_corp_user(new_user.corp_id, new_user.company_name, new_user.company_address,new_user.reference_person_name,new_user.reference_person_phone, new_user.reference_person_email,new_user.invoices_email, new_user.password)
                            os.system("cls")
                            print("Corporate User registration successful")


                        except Exception as e:
                            print(e)
                            break

                    # Remove a Corporate user                         
                    elif sub_choice == '2':
                        
                        corp_id = input("Enter user ID to remove (10-Digits): ")
                        if csv_operator.corp_user_exists(corp_id):
                            csv_operator.remove_corp_user(corp_id)
                        else:
                            print(f"user >{corp_id}< does not exist.")

                    # Update a corp user
                    elif sub_choice == '3':
                        
                        corp_id = input("Enter user ID to update (10-Digits): ")
                        if csv_operator.corp_user_exists(corp_id):
                            updated_data = {
                                            "corp_id": None,
                                            "company_name": None,
                                            "company_address": None,
                                            "reference_person_name": None,
                                            "reference_person_phone": None,
                                            "reference_person_email": None,
                                            "invoices_email":None,
                                            "password": None
                                            }

                            while True:  # Keep prompting until valid input
                                company_name = input("Enter company name: ")
                                if valid.valid_company_name(company_name):
                                    updated_data["company_name"] = company_name
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Name: {company_name}")

                            while True:  # Keep prompting until valid input
                                company_address = input("Enter company address (StreetName BuildingNumber PostNumber City ): ")
                                if valid.valid_address(company_address):
                                    updated_data["company_address"] = company_address
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid company address (ex:lindängsvägen 21 52320 Götebörg ): {company_address}")
                            
                            while True:
                                reference_person_name= input("Enter the reference person name (firstName LastName): ")
                                if valid.valid_name(reference_person_name):
                                    updated_data["reference_person_name"] = reference_person_name
                                    break
                                else:
                                    print(f"[!] Invalid Name (John Smith): {reference_person_name}")

                            while True:  # Keep prompting until valid input
                                reference_person_phone = input("Enter reference person phone number(10-digits must start with 07): ")
                                if valid.valid_phone(reference_person_phone):
                                    updated_data["reference_person_phone"] = reference_person_phone
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Phone number (ex: 0712121212): {reference_person_phone}")

                            while True:  # Keep prompting until valid input
                                reference_person_email = input("Enter reference person email(ex: info@gmail.com): ")
                                if valid.valid_email(reference_person_email):
                                    updated_data["reference_person_email"] = reference_person_email
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {reference_person_email}")

                            while True:  # Keep prompting until valid input
                                invoices_email = input("Enter invoices email (ex: info@gmail.com): ")
                                if valid.valid_email(invoices_email):
                                    updated_data["invoices_email"] = invoices_email
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Email: {invoices_email}")

                            while True:  # Keep prompting until valid input
                                password = input("Enter password (Atleast 1 capital letter and one special character): ")
                                if valid.valid_password(password):
                                    updated_data["password"] = password
                                    break  # Exit the loop when input is valid
                                else:
                                    print(f"[!] Invalid Password (ex: K.aaa): {password}")

                            csv_operator.update_corp_user(corp_id, updated_data)
                            os.system("cls")
                            print(f"User {user_id} updated successfully.")
                        else:
                            print(f"user >{corp_id}< does not exist.")

                    # Search corp users
                    elif sub_choice == "4":
                        user_id = input("Enter user ID (10-Digits): ")
                        user_info = csv_operator.find_corp_user(user_id)
                        
                        if user_info:
                            # User exists, print out the user info
                            print(f"User Info:\n{user_info}")
                        else:
                            print(f"user >{corp_id}< does not exist.")
                        

                    elif sub_choice == '5':
                        # Return to the main menu
                        os.system("cls")
                        break

                    else:
                        print("Invalid choice. Please select a valid option (1-4) in the sub-menu.")

            # Submenu for  vehicle management
            elif choice == '3':
                while True:
                    print("       > Vehicles <    ")
                    print("1. Add Bike to the system")
                    print("2. Add a Truck to the System")
                    print("3. Add a Boat to the system")
                    print("4. Search vehicles")
                    print("5. Back to Main Menu")
                    sub_choice = input("Enter your choice (1-4): ")
                    os.system("cls")
                    csv_operator = CSV_OP()

                    # Add Bike
                    if sub_choice == "1":
                        try:
                            while True:
                                # Prompt the user for a vehicle ID
                                vehicle_id = input("Enter vehicle Vent number ('123ABC'): ")

                                if valid.valid_vent_num(vehicle_id):
                                    # Check if the vehicle with the given ID already exists
                                    if csv_operator.vehicle_exists(vehicle_id):
                                        print(f"Vehicle with ID {vehicle_id} already exists.")
                                    else:
                                        # Prompt the user for the vehicle name
                                        vehicle_name = input("Enter vehicle name:")

                                        location = Vehicle.get_location("Sweden")
                                        # Create a bike-type vehicle with the stats of a bike
                                        vehicle_data = {
                                            "id": vehicle_id,
                                            "name": vehicle_name,
                                            "max_capacity_kg": 10,  # Example value for bike capacity in kilograms
                                            "max_capacity_items": 2,  # Example value for bike capacity in items
                                            "location": location,  # Set the default location
                                            "type": "Bike",  # Set the type to "Bike"
                                            "status": "Free"  # Set the status to "Free"
                                        }

                                        # Add the bike-type vehicle to the CSV
                                        csv_operator.create_vehicles(vehicle_data)
                                        print(f"Vehicle with ID {vehicle_id} has been added as a bike.\n")

                                        # Provide an option to go back to the vehicle management submenu
                                        add_more = input("Do you want to add more vehicles? (Y/N): ")
                                        if add_more.lower() != "y":
                                            os.system("cls")
                                            break
                                else:
                                    print(f"[!] Invalid ID (ex:123ABC): {vehicle_id}")

                        except Exception as e:
                            print(e)
                    
                    # Add Truck
                    elif sub_choice == "2":
                        try:
                            while True:
                                # Prompt the user for a vehicle ID
                                vehicle_id = input("Enter vehicle ID ('123ABC'): ")
                                if valid.valid_vent_num(vehicle_id):
                                    # Check if the vehicle with the given ID already exists
                                    if csv_operator.vehicle_exists(vehicle_id):
                                        print(f"Vehicle with ID {vehicle_id} already exists.")
                                    else:
                                        # Prompt the user for the vehicle name
                                        vehicle_name = input("Enter vehicle name: ")
                                        
                                        location= Vehicle.get_location("Sweden")
                                        # Create a bike-type vehicle with the stats of a bike
                                        vehicle_data = {
                                            "id": vehicle_id,
                                            "name": vehicle_name,
                                            "max_capacity_kg": 10,  # Example value for bike capacity in kilograms
                                            "max_capacity_items": 2,  # Example value for bike capacity in items
                                            "location": location,  # Set the default location
                                            "type": "Truck",  # Set the type to "Bike"
                                            "status": "Free"  # Set the status to "Free"
                                        }

                                        # Add the bike-type vehicle to the CSV
                                        csv_operator.create_vehicles(vehicle_data)
                                        print(f"Vehicle with ID {vehicle_id} has been added as a Truck.\n")
                                        
                                        # Provide an option to go back to the vehicle management submenu
                                        add_more = input("Do you want to add more vehicles? (Y/N): ")
                                        if add_more.lower() != "y":
                                            os.system("cls")
                                            break

                                else:
                                    print(f"[!] Invalid ID (ex: 123ABC): {vehicle_id}")
                        except Exception as e:
                            print(e)

                    # Add a boat
                    elif sub_choice == "3":
                        try:
                            while True:
                                # Prompt the user for a vehicle ID
                                vehicle_id = input("Enter vehicle ID ('123ABC'): ")
                                if valid.valid_vent_num(vehicle_id):
                                    # Check if the vehicle with the given ID already exists
                                    if csv_operator.vehicle_exists(vehicle_id):
                                        print(f"Vehicle with ID {vehicle_id} already exists.")
                                    else:
                                        # Prompt the user for the vehicle name
                                        vehicle_name = input("Enter vehicle name: ")
                                        
                                        location= Vehicle.get_location("Sweden")
                                        # Create a bike-type vehicle with the stats of a bike
                                        vehicle_data = {
                                            "id": vehicle_id,
                                            "name": vehicle_name,
                                            "max_capacity_kg": 10,  # Example value for bike capacity in kilograms
                                            "max_capacity_items": 2,  # Example value for bike capacity in items
                                            "location": location,  # Set the default location
                                            "type": "Boat",  # Set the type to "Bike"
                                            "status": "Free"  # Set the status to "Free"
                                        }

                                        # Add the bike-type vehicle to the CSV
                                        csv_operator.create_vehicles(vehicle_data)
                                        print(f"Vehicle with ID {vehicle_id} has been added as a Boat.\n")

                                        # Provide an option to go back to the vehicle management submenu
                                        add_more = input("Do you want to add more vehicles? (Y/N): ")
                                        if add_more.lower() != "y":
                                            os.system("cls")
                                            break
                                else:
                                    print(f"[!] Invalid ID (ex: 123ABC) {vehicle_id}")
                        except Exception as e:
                            print(e)
                    
                    # search Vehicle
                    elif sub_choice == "4":
                        try:
                            # Prompt the user for a vehicle ID to search for
                            vehicle_id = input("Enter vehicle ID to search for (123ABC): ")
                            
                            # Call the find_vehicle method to search for the vehicle
                            vehicle_info = csv_operator.find_vehicle(vehicle_id)
                            
                            if vehicle_info:
                                # Vehicle exists, print out the vehicle info
                                print(f"Vehicle Info:\n{vehicle_info}")
                            else:
                                print(f"Vehicle with ID {vehicle_id} does not exist.")
                        except Exception as e:
                            print(e)

                     # Return to the main menu

                    # Return to MainMenu
                    elif sub_choice == '5':
                        os.system("cls")
                        break

                    else:
                        print("Invalid choice. Please select a valid option (1-5) in the sub-menu.")
                        
            # Submenu for orders  management 
            elif choice == '4':
                while True:
                    print("\n        > Orders <    ")
                    print("1. Add an order to the system")
                    print("2. Add items to an order")
                    print("3. Update order status")
                    print("4. Search orders")
                    print("5. Search order status")
                    print("6. Back to Main Menu")
                    sub_choice = input("Enter your choice (1-6): ")
                    os.system("cls")
                    csv_operator = CSV_OP()

                    # add orders to the system
                    if sub_choice == "1":
                            while True:
                                # Generate a unique order ID
                                generated_order_id = Order.generate_order_id()
                                
                                # prompt to select items
                                selected_items = []
                                total_weight = 0  
                                total_price= 0
                                sender = {}  # Initialize the sender dictionary
                                
                                items = csv_operator.get_items()
                                print("\n> Available items <")
                                for index, item in enumerate(items):
                                    print(f"{index + 1}. {item['name']} - Price: {item['price_per_kg']} - Shop: {item['shop_name']}")

                                while True:
                                    if not items:
                                        print("No items available.")
                                        break  # Exit the loop if there are no items

                                    user_input = input("Enter the item number to select (or 'done' to finish): ")

                                    if user_input.lower() == 'done':
                                        os.system("cls")
                                        break  # Exit the loop if the user is done   

                                    else:
                                        try:
                                            item_number = int(user_input) - 1
                                            if 0 <= item_number < len(items):
                                                selected_item = items[item_number]
                                                selected_items.append(selected_item)

                                                # Calculate and store the total weight as you add items
                                                total_weight += selected_item['weight']
                                                # Calculate and store the total price as you add items
                                                total_price += selected_item['price_per_kg']
                                                # Get the shop_name from the selected item and add it to the sender dictionary
                                                sender[selected_item['name']] = selected_item['shop_name']
                                            

                                            else:
                                                print("Invalid item number. Please try again.")
                                        except ValueError:
                                            print("Invalid input. Please enter a valid item number or 'done'.")

                                # Print all the selected items
                                print("\nSelected items:")
                                for item in selected_items:
                                    print(f"{item['name']} - Price: {item['price_per_kg']}")
                            
                                print()
                                print(f"Total weight of selected items: {total_weight} kg")
                                print(f"Total price of selected items: ${total_price:.2f}")# Print the sender dictionary
                                print("\nSender information:")

                                for item_name, shop_name in sender.items():
                                    print(f"Item: {item_name} - Sender: {shop_name}")
                    

                                # Get the list of available vehicles
                                available_vehicles = [vehicle for vehicle in csv_operator.get_vehicles() if vehicle["status"] == "Free" and vehicle['max_capacity_kg'] >= total_weight]
                                # Check if there are any free vehicles
                                if not available_vehicles:
                                    print("No free vehicles available.")
                                else:
                                    # Prompt the user to select an available vehicle
                                    while True:
                                        print("\n> Available vehicles <")
                                        for index, vehicle in enumerate(available_vehicles):
                                            print(f"{index + 1}. Vehicle ID: {vehicle['id']} // Name: {vehicle['name']} // max_capacity_kg:{vehicle["max_capacity_kg"]} // max_capacity_items:{vehicle["max_capacity_items"]} // type: {vehicle["type"]} // status:{vehicle["status"]} // Location: {vehicle['location']}")

                                        user_input = input("Enter the number of the vehicle to select (or 'done' to finish): ")

                                        if user_input.lower() == 'done':
                                            break  # Exit the loop if the user is done
                                        else:
                                            try:
                                                vehicle_number = int(user_input) - 1
                                                if 0 <= vehicle_number < len(available_vehicles):
                                                    selected_vehicle = available_vehicles[vehicle_number]
                                                    print(f"\nSelected Vehicle ID: {selected_vehicle['id']} - Name: {selected_vehicle['name']}")
                                                    # You can use the selected vehicle as needed
                                                    break
                                                else:
                                                    print("Invalid vehicle number. Please try again.")
                                            except ValueError:
                                                print("Invalid input. Please enter a valid vehicle number or 'done'.")

                                customer= None
                                # Prompt the user to enter a user ID (customer)
                                while True:
                                    user_id = input("\nEnter user ID for the customer (10-digits):  ")
                                    customer_info = csv_operator.get_customer(user_id)
                                    if customer_info:
                                        customer = customer_info
                                        break
                                    else:
                                        print(f"User with ID {user_id} does not exist. Please enter a valid user ID.")

                                # prompt the user to enter delivery address
                                to_location = None
                                while to_location is None:
                                    address = input("\nEnter delivery adress (StreetName BuildingNumber PostNumber City ): ")
                                    if valid.valid_address(address):
                                        to_location = address
                                    else:
                                        print("[!]Invalid address (ex:lindängsvägen 21 52320 Götebörg ): ")

                                # Prompt the user to enter order priority
                                while True:
                                    order_priority = input("\nEnter order priority (L for Low, M for Medium, H for High): ").lower()
                                    if order_priority in ["l", "m", "h"]:
                                        order_priority = "Low" if order_priority == "l" else "Medium" if order_priority == "m" else "High"
                                        break
                                    else:
                                        print("Invalid order priority. Please enter 'L' for Low, 'M' for Medium, or 'H' for High.")
                                
                                # Payment Process
                                while True:
                                    print(f"\nthe total price for selected items: {total_price}$")
                                    payment_method = input("select payment method (1 for Credit/Debit Card, 2 for Bank Transfer, or 0 to exit): ")
                                    
                                    # Card Payment
                                    if payment_method == "1":
                                        generated_transaction_id = Payment.generate_transaction_id()
                                        while True:
                                            card_number = input("\nEnter card number: ")

                                            if valid.valid_card_num(card_number):
                                                break
                                            else:
                                                print("Invalid card number. (16-digits)")

                                        while True:
                                            card_holder_name = input("\nEnter card holder's name: ")

                                            if valid.valid_name(card_holder_name):
                                                self.payment_method = "card-payment"
                                                self.card_number = card_number
                                                self.card_holder_name = card_holder_name
                                                self.payment_status = "paid"
                                                self.transaction_id = Payment.generate_transaction_id()
                                                print("\nCard payment details accepted.")
                                                os.system("cls")
                                                break
                                            else:
                                                print("Invalid card holder name. Please try again.")
                                        csv_operator.add_card_info(user_id, card_number, card_holder_name)
                                        csv_operator.add_payment_info(generated_transaction_id, user_id, total_price, "Credit/Debit Card", "paid")
                                        break

                                    # Bank Transfer
                                    elif payment_method == "2":
                                        generated_transaction_id = Payment.generate_transaction_id()
                                        while True:
                                            account_number = input("\nEnter account number: ")

                                            if valid.valid_account_num(account_number):
                                                break
                                            else:
                                                print("Invalid account number. (20-digits)")

                                        while True:
                                            account_holder_name = input("\nEnter card holder's name: ")

                                            if valid.valid_name(account_holder_name):
                                                self.payment_method = "Bank-Transfer"
                                                self.account_number = account_number
                                                self.account_holder_name = account_holder_name
                                                self.payment_status = "paid"
                                                self.transaction_id = Payment.generate_transaction_id()
                                                print("\naccount payment details accepted.")
                                                os.system("cls")
                                                break
                                            else:
                                                print("Invalid account holder name. Please try again.")
                                        csv_operator.add_bank_info(user_id, account_number, account_holder_name)
                                        csv_operator.add_payment_info(generated_transaction_id, user_id, total_price, "Credit/Debit Card", "paid")
                                        break
                                  
                                    # exit menu
                                    elif payment_method == "0":
                                        os.system("cls")
                                        break
                                    
                                    else: 
                                        print("Invalid choice. Please enter 1, 2, or 0.")
                               
                                # Create a dictionary with payment details
                                payment_details = {
                                    "transaction_id": generated_transaction_id,
                                    "user_id": user_id,
                                    "amount": total_price,
                                    "payment_method": "Credit/Debit Card" if payment_method == "1" else "Bank Transfer",
                                    "payment_status": "paid"
                                }

                                
                                # Create an order with the generated order ID
                                new_order = Order(
                                    order_id=generated_order_id,
                                    order_priority=order_priority,
                                    sender=sender,
                                    customer= customer,
                                    to_location=to_location,
                                    payment_details=payment_details,
                                    items=items,
                                    total_weight=total_weight,
                                    order_status="processing",
                                    vehicle=vehicle,
                                    total_price= total_price
                                )
                                
                                for item in selected_items:
                                    new_order.items.append(item['name'])
                                
                                # Add the new order to the system (you should implement this method)
                                csv_operator.add_order(
                                order_id= generated_order_id,
                                order_priority=new_order.order_priority,
                                sender=new_order.sender,
                                to_location=new_order.to_location,
                                items=new_order.items,
                                payment_details=new_order.payment_details,
                                total_weight=new_order.total_weight,
                                order_status=new_order.order_status,
                                vehicle=new_order.vehicle,
                                total_price= total_price
                            )
                                print(f"Order with ID > {generated_order_id} < has been added.(>>>important<<<)")
                                break

                    # Add items to an existing order
                    if sub_choice == "2":
                        while True:
                            order_id = input("Enter the order ID to add items to (or 'exit' to go back): ")

                            if order_id.lower() == 'exit':
                                os.system("cls")
                                break  # Exit the loop if the user enters 'exit'

                            order_info = csv_operator.get_order(order_id)

                            if order_info is not None:
                                # Order found, you can proceed to add items to it
                                print(f"Order > {order_id} < found. You can now add items to it.")
                                # Display the current items in the order
                                current_items = order_info["items"].split(",") if order_info["items"] else []
                                if current_items:
                                    print("Current items in the order:")
                                    for index, item in enumerate(current_items):
                                        print(f"{index + 1}. {item}")

                                updated_items = []
                                items = csv_operator.get_items()
                                print("\n> Available items <")
                                for index, item in enumerate(items):
                                    print(f"{index + 1}. {item['name']} - Price: {item['price_per_kg']} - Shop: {item['shop_name']}")

                                while True:
                                    if not items:
                                        print("No items available.")
                                        break  # Exit the loop if there are no items

                                    user_input = input("Enter the item number to select (or 'done' to finish): ")

                                    if user_input.lower() == 'done':
                                        os.system("cls")

                                        # Calculate the total weight of the updated items
                                        total_weight_updated = sum(item['weight'] for item in updated_items)
                                        # Calculate the total price of the updated items
                                        total_price_updated = sum(item['price_per_kg'] for item in updated_items)

                                        # Convert the updated_items list into a comma-separated string
                                        updated_items_str = ", ".join(item['name'] for item in updated_items)

                                        # Retrieve the existing total price from order_info and handle empty case
                                        if order_info["total_price"]:
                                            total_price = float(order_info["total_price"])
                                        else:
                                            total_price = 0.0

                                        # Retrieve the existing total weight from order_info and handle empty case
                                        if order_info["total_weight"]:
                                            total_weight = float(order_info["total_weight"])
                                        else:
                                            total_weight = 0.0

                                        # Update the order with the new items, total weight, and total price
                                        csv_operator.update_order(order_id, updated_items_str, total_weight + total_weight_updated, total_price + total_price_updated)
                                        print(f"Order with id > {order_id} < has been updated")
                                        break  # Exit the loop if the user is done

                                    else:
                                        try:
                                            item_number = int(user_input) - 1
                                            if 0 <= item_number < len(items):
                                                selected_item = items[item_number]
                                                updated_items.append(selected_item)
                                            else:
                                                print("Invalid item number. Please try again.")

                                        except ValueError:
                                            print("Invalid input. Please enter a valid item number or 'done'.")
                                break
                            else:
                                print(f"Invalid order ID. Order with ID > {order_id} < not found. Please enter a valid order ID.")

                    # Update order status
                    if sub_choice == "3":
                        while True:
                            order_id = input("Enter the order ID to update the order status (or 'exit' to go back): ")

                            if order_id.lower() == 'exit':
                                os.system("cls")
                                break  # Exit the loop if the user enters 'exit'

                            order_info = csv_operator.get_order(order_id)

                            if order_info is not None:
                                # Order found, you can proceed to update the order status
                                print(f"Order > {order_id} < found. You can now update the order status.")

                                # Display the current order status
                                current_status = order_info["order_status"]
                                print(f"Current order status: {current_status}")

                                # Define the available order statuses
                                order_statuses = ["Delivered", "Processing", "Canceled"]

                                # Display the available order statuses with numbers
                                for index, status in enumerate(order_statuses, start=1):
                                    print(f"{index}. {status}")

                                while True:
                                    # Prompt the user to select a status by number
                                    user_input = input("Enter the number of the new order status: ")

                                    if user_input.isdigit():
                                        selected_status_index = int(user_input) - 1
                                        if 0 <= selected_status_index < len(order_statuses):
                                            new_status = order_statuses[selected_status_index]
                                            # Update the order status in the CSV file
                                            csv_operator.update_order_status(order_id, new_status)
                                            os.system("cls")
                                            print(f"Order status updated to: {new_status}")
                                            break
                                        else:
                                            print("Invalid number. Please select a valid number.")
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                            else:
                                print(f"Invalid order ID. Order with ID > {order_id} < not found. Please enter a valid order ID.")

                    # Search orders
                    if sub_choice == "4":
                        while True:
                            order_id = input("Enter the order ID to search for (or 'exit' to go back): ")

                            if order_id.lower() == 'exit':
                                os.system("cls")
                                break  # Exit the loop if the user enters 'exit'

                            order_info = csv_operator.get_order(order_id)

                            if order_info is not None:
                                # Order found, you can now work with the order information
                                print(f"Order > {order_id} < information:\n")
                                for key, value in order_info.items():
                                    print(f"{key}: {value}")

                            else:
                                print(f"Order with ID > {order_id} < not found. Please enter a valid order ID.")
                    
                    #Get updated status:
                    if sub_choice == "5":
                        while True:
                            order_id = input("Enter the order ID to get the order status (or 'exit' to go back): ")

                            if order_id.lower() == 'exit':
                                os.system("cls")
                                break  # Exit the loop if the user enters 'exit'

                            order_info = csv_operator.get_order(order_id)

                            if order_info is not None:
                                # Order found, display the order status
                                order_status = order_info.get("order_status")
                                if order_status:
                                    print(f"\nOrder > {order_id} < status: {order_status}\n")
                                else:
                                    print(f"Order > {order_id} < has no status information.")
                            else:
                                print(f"Order with ID > {order_id} < not found. Please enter a valid order ID.")

                    #return to Mainmenu
                    if sub_choice == "6":
                        break
                
            # Vehicle Selection
            elif choice == '5':
                csv_operator = CSV_OP()
                print("Vehicle Selection:\n")
                
                while True:
                    try:
                        total_weight = float(input("\nEnter the total weight of the shipment: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number(123.123).")
                        continue  # Continue the loop if there's an invalid input
                    try:
                        total_items = int(input("Enter the total number of items in the shipment: "))

                    except ValueError:
                        print("Invalid input. Please enter a valid number(123.123).")
                        continue  # Continue the loop if there's an invalid input

                    best_vehicle = csv_operator.select_vehicle(total_weight, total_items)
                    
                    if best_vehicle:
                        print(f"The best vehicle for the shipment has ID: {best_vehicle['id']}")
                        break  # Exit the loop if a suitable vehicle is found
                    else:
                        print("No suitable vehicles available for the shipment.")
            
            # Exit
            elif choice == '6':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option (1-12).")

