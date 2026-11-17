from datetime import timedelta

class PricingManager:
    def calculate_rental_price(self, bike, start_datetime, expected_return_datetime):
        duration = expected_return_datetime - start_datetime

        if duration.days == 0:
            hours = duration.seconds // 3600
            if duration.seconds % 3600 != 0:
                hours += 1
            return hours * bike.hourly_price

        days = duration.days
        remaining_hours = duration.seconds // 3600

        if duration.seconds % 3600 != 0:
            remaining_hours += 1

        price = days * bike.daily_price
        price += remaining_hours * bike.hourly_price
        return price

    def calculate_late_fee(self, expected_return_datetime, actual_return_datetime):
        delay = actual_return_datetime - expected_return_datetime

        if delay <= timedelta(0):
            return 0
        elif delay <= timedelta(hours=1):
            return 20
        elif delay <= timedelta(hours=3):
            return 50
        else:
            return 100