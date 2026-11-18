class BikeManager:
    def __init__(self, bikes, data_manager):
        self.bikes = bikes
        self.data_manager = data_manager
        
    def get_all_bikes(self):
        return self.bikes
    
    def find_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id:
                return bike
        return None
    
    def get_available_bikes(self):
        available_bikes = []
        for bike in self.bikes:
            if bike.is_available and bike.is_operational:
                available_bikes.append(bike)
        return available_bikes
    
    def save_bikes(self):
        self.data_manager.save_bikes(self.bikes)
        
        
    def add_bike(self, bike):
        if self.find_bike(bike.bike_id):
            return False
        self.bikes.append(bike)
        self.save_bikes()
        return True
    
    
    def update_bike(self, bike_id, model, bike_type, hourly_price, daily_price):
        bike = self.find_bike(bike_id)
        if not bike:
            return False
        bike.model = model
        bike.bike_type = bike_type
        bike.hourly_price = hourly_price
        bike.daily_price = daily_price
        
        self.save_bikes()
        return True
    
    def set_bike_operational(self, bike_id, status):
        bike =self.find_bike(bike_id)
        if not bike:
            return False
        bike.set_operational(status)
        if not status:
            bike.set_available(False)
        self.save_bikes()
        return True