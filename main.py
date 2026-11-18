from managers.data_manager import DataManager
from managers.report_manager import ReportManager


def main():
    data_manager = DataManager()

    bikes = data_manager.load_bikes()
    rentals = data_manager.load_rentals()

    report_manager = ReportManager(bikes, rentals)

    print("Total rentals:", report_manager.get_total_rentals())
    print("Active rentals:", report_manager.get_active_rentals_count())
    print("Completed rentals:", report_manager.get_completed_rentals_count())
    print("Total revenue:", report_manager.get_total_revenue())
    print("Late fees:", report_manager.get_total_late_fees())
    print("Average rental price:", report_manager.get_average_rental_price())
    print("Top customer:", report_manager.get_top_customer())

    top_bike = report_manager.get_most_rented_bike()
    print("Most rented bike:", top_bike.bike_id if top_bike else None)

if __name__ == "__main__":
    main()