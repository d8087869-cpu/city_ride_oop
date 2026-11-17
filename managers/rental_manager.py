from models.rental import Rental

class RentalManager:
    def __init__(self, bikes, rentals, pricing_manager):
        self.bikes = bikes
        self.rentals = rentals
        self.pricing_manager = pricing_manager

    def find_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id:
                return bike
        return None

    def check_bike_availability(self, bike_id):
        bike = self.find_bike(bike_id)

        if bike is None:
            return False

        if not bike.is_operational:
            return False

        if not bike.is_available:
            return False

        return True

    def find_rental(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def create_rental(self, rental_id, customer_name, bike_id,
                      start_datetime, expected_return_datetime):

        bike = self.find_bike(bike_id)

        if bike is None:
            return None

        if not self.check_bike_availability(bike_id):
            return None

        if expected_return_datetime <= start_datetime:
            return None

        total_price = self.pricing_manager.calculate_rental_price(bike, start_datetime, expected_return_datetime)

        rental = Rental(
            rental_id,
            customer_name,
            bike_id,
            start_datetime,
            expected_return_datetime,
            None,
            total_price,
            0,
            "Active")
        self.rentals.append(rental)
        bike.set_available(False)
        return rental
    
        
    def get_customer_rentals(self, customer_name):
        customer_rentals = []
        for rental in self.rentals:
            if rental.customer_name == customer_name:
                customer_rentals.append(rental)
        return customer_rentals

    def get_active_rentals(self):
        active_rentals = []
        for rental in self.rentals:
            if rental.status == "Active":
                active_rentals.append(rental)
        return active_rentals
    
    
    def return_bike(self, rental_id, return_datetime):
        rental = self.find_rental(rental_id)
        if rental is None:
            return None
        if rental.status != "Active":
                return None

        bike = self.find_bike(rental.bike_id)
        if bike is None:
            return None

        late_fee = self.pricing_manager.calculate_late_fee(rental.expected_return_datetime, return_datetime)
        rental.complete_rental(return_datetime, late_fee)
        bike.set_available(True)
        return rental