from validation import Validations as valid


class Vehicle:
    def __init__(self, id, name, max_capacity_kg, max_capacity_items, location, vehicle_type):
        self.name = name
        self.id = None
        self.max_capacity_kg = max_capacity_kg
        self.max_capacity_items = max_capacity_items
        self.left_capacity_kg = max_capacity_kg
        self.left_capacity_items = max_capacity_items
        self.current_position = None
        # The default status is Free
        self.current_status = "Free"  
        self.location = location
        self.vehicle_type = vehicle_type

        if valid.valid_vent_id(id):
            self.id = id

    # create a location for each country
    def get_location(country_name):
        # Define a dictionary mapping country names to coordinates
        countries = {
            "Sweden": ("18.6435", "59.3326"),
            "OtherCountry": ("other_longitude", "other_latitude"),
            # Add more countries and their coordinates here
        }
        
        # Check if the provided country_name exists in the dictionary
        if country_name in countries:
            # Retrieve the coordinates for the given country
            coordinates = countries[country_name]
            return f"{coordinates[0]}, {coordinates[1]}, {country_name}"
        else:
            return "Country not found"








###Genereate Vehicles###
# import csv
#  # # Define the data for vehicles (bikes, trucks, and boats)
# vehicle_data = [
#      {"id": "001ABC", "name": "Bike1", "max_capacity_kg": 10, "max_capacity_items": 2, "location": Location(18.6435, 59.3326, "Sweden")},
#      {"id": "002DEF", "name": "Bike2", "max_capacity_kg": 10, "max_capacity_items": 2, "location": Location(18.0632, 59.3293, "Sweden")},
#      {"id": "003GHI", "name": "Bike3", "max_capacity_kg": 10, "max_capacity_items": 2, "location": Location(17.9680, 59.3861, "Sweden")},
#      {"id": "004JKL", "name": "Bike4", "max_capacity_kg": 10, "max_capacity_items": 2, "location": Location(18.0727, 59.3135, "Sweden")},
#      {"id": "005MNO", "name": "Truck1", "max_capacity_kg": 3000, "max_capacity_items": 100, "location": Location(18.0632, 59.3293, "Sweden")},
#      {"id": "006PQR", "name": "Truck2", "max_capacity_kg": 3000, "max_capacity_items": 100, "location": Location(17.9734, 59.3599, "Sweden")},
#      {"id": "007STU", "name": "Boat1", "max_capacity_kg": 100000, "max_capacity_items": 10000, "location": Location(18.0727, 59.3135, "Sweden")},
#      {"id": "008VWX", "name": "Boat2", "max_capacity_kg": 100000, "max_capacity_items": 10000, "location": Location(17.9900, 59.3266, "Sweden")},
#  ]

#  #CSV file path
# csv_file = "exam_2/csv_files/vehicles.csv"

# # # Write the vehicle data to the CSV file
# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#      fieldnames = ["id", "name", "max_capacity_kg", "max_capacity_items", "location"]
#      writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
#      writer.writeheader()

#      for vehicle in vehicle_data:
#          writer.writerow(vehicle)
# print(f"Vehicle data has been written to '{csv_file}'.")