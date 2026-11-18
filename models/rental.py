from datetime import datetime


class Rental:
    def __init__(self, rental_id, customer_name, bike_id,
                 start_datetime, expected_return_datetime,
                 actual_return_datetime, total_price, late_fee, status):
        self.rental_id = rental_id
        self.customer_name = customer_name
        self.bike_id = bike_id
        self.start_datetime = start_datetime
        self.expected_return_datetime = expected_return_datetime
        self._actual_return_datetime = actual_return_datetime
        self.total_price = total_price
        self._late_fee = late_fee
        self._status = status

    @property
    def status(self):
        return self._status

    @property
    def actual_return_datetime(self):
        return self._actual_return_datetime

    @property
    def late_fee(self):
        return self._late_fee


    def complete_rental(self, return_datetime, late_fee):
        if self._status == "Completed":
            return False
        self._actual_return_datetime = return_datetime
        self._late_fee = late_fee
        self._status = "Completed"
        return True

    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "customer_name": self.customer_name,
            "bike_id": self.bike_id,
            "start_datetime": self.start_datetime.isoformat(),
            "expected_return_datetime": self.expected_return_datetime.isoformat(),
            "actual_return_datetime": self.actual_return_datetime.isoformat()
            if self.actual_return_datetime else None,
            "total_price": self.total_price,
            "late_fee": self.late_fee,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["rental_id"],
            data["customer_name"],
            data["bike_id"],
            datetime.fromisoformat(data["start_datetime"]),
            datetime.fromisoformat(data["expected_return_datetime"]),
            datetime.fromisoformat(data["actual_return_datetime"])
            if data["actual_return_datetime"] else None,
            data["total_price"],
            data["late_fee"],
            data["status"])