class Bike:
    def __init__(self, bike_id, model, bike_type, hourly_price,
                 daily_price, is_available, is_operational):
        self.bike_id = bike_id
        self.model = model
        self.bike_type = bike_type
        self.hourly_price = hourly_price
        self.daily_price = daily_price
        self._is_available = is_available
        self._is_operational = is_operational
        
    @property
    def is_available(self):
        return self._is_available


    @is_available.setter
    def is_available(self, status):
        if status and not self._is_operational:
            self._is_available = False
        else:
            self._is_available = status

    @property
    def is_operational(self):
        return self._is_operational


    def set_available(self, status):
        self.is_available = status

    def set_operational(self, status):
        self._is_operational = status

        if not status:
            self._is_available = False
            
        if not self._is_operational:
            self._is_available = False

    def to_dict(self):
        return {
            "bike_id": self.bike_id,
            "model": self.model,
            "bike_type": self.bike_type,
            "hourly_price": self.hourly_price,
            "daily_price": self.daily_price,
            "is_available": self.is_available,
            "is_operational": self.is_operational
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["bike_id"],
            data["model"],
            data["bike_type"],
            data["hourly_price"],
            data["daily_price"],
            data["is_available"],
            data["is_operational"]
        )