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
    
    
    def get_total_revenue(self):
        total = 0 
        for rental in self.rentals:
            if rental.status == "Completed":
                total += rental.total_price
        return total
    
    
    def get_total_late_fees(self):
        total = 0 
        for rental in self.rentals:
            total += rental.late_fee
        return total
    
    def get_average_rental_price(self):
        if len(self.rentals) == 0:
            return 0
        total = 0
        for rental in self.rentals:
            total += rental.total_price
        return total / len(self.rentals)
    
    
    def get_top_customer(self):
        customer_counts = {}
        for rental in self.rentals:
            customer = rental.customer_name
            if customer not in customer_counts:
                customer_counts[customer] = 0
            customer_counts[customer] += 1
        if len(customer_counts) == 0:
            return None
        
        top_customer = None
        max_count = 0
        for customer, count in customer_counts.items():
            if count > max_count:
                max_count = count
                top_customer = customer
        return top_customer
        
    
    
    def get_most_rented_bike(self):
        bike_counts = {}
        for rental in self.rentals:
            bike_id = rental.bike_id
            if bike_id not in bike_counts:
                bike_counts[bike_id] = 0
            bike_counts[bike_id] += 1 
        if len(bike_counts) == 0:
            return None
    
        top_bike_id = None
        max_count = 0
        for bike_id, count in bike_counts.items():
            if count > max_count:
                max_count = count
                top_bike_id = bike_id
        for bike in self.bikes:
            if bike.bike_id == top_bike_id:
                return bike
        return None