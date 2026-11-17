import json
from models.bike import Bike
from models.rental import Rental

class DataManager:
    def __init__(self):
        self.bikes_file = "data/bikes.json"
        self.rentals_file = "data/rentals.json"
    
    def load_bikes(self):
        with open(self.bikes_file, "r") as file:
            bikes_data = json.load(file)
        bikes = []
        for bike_data in bikes_data:
            bike= Bike.from_dict(bike_data)
            bikes.append(bike)
        return bikes
    
    def load_rental(self):
        with open(self.rentals_file, "r") as file:
            rentals_data = json.load(file)
        rentals = []
        for rental_data in rentals_data:
            rental = Rental.from_dict(rental_data)
            rentals.append(rental)
        return rentals

    def save_bikes(self, bikes):
        bikes_data = []
        for bike in bikes:
            bikes_data.append(bike.to_dict())
        with open(self.bikes_file, "w") as file:
            json.dump(bikes_data, file, indent=4)

    def save_rentals(self, rentals):
        rentals_data = []
        for rental in rentals:
            rentals_data.append(rental.to_dict())
        with open(self.rentals_file, "w") as file:
            json.dump(rentals_data, file, indent=4)