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
        self.actual_return_datetime = actual_return_datetime
        self.total_price = total_price
        self.late_fee = late_fee
        self.status = status

    def complete_rental(self, return_datetime, late_fee):
        self.actual_return_datetime = return_datetime
        self.late_fee = late_fee
        self.status = "Completed"

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