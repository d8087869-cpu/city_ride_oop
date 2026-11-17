class ReportManager:
    def __init__(self, bikes, rentals):
        self.bikes = bikes
        self.rentals =rentals

    def get_total_rentals(self):
        return len(self.rentals)

    def get_active_rentals_count(self):
        count = 0
        for rental in self.rentals:
            if rental.status == "Active":
                count += 1 
        return count

    def get_completed_rentals_count(self):
        count = 0 
        for rental in self.rentals:
            if rental.status == "Completed":
                count += 1
        return count