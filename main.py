from data_generator import generate_flight_data
from data_loader import load_all_data
from data_processor import process_data

def log_results(total_records, dirty_records, top_city_stats, max_arrival_city, max_departure_city):
    """Logs results to the console."""
    print(f"Total records processed: {total_records}")
    print(f"Total dirty records: {dirty_records}")
    print("\nTop Cities by Flight Duration:")
    print(top_city_stats)

    print(f"\nCity with MAX passengers arrived: {max_arrival_city}")
    print(f"City with MAX passengers departed: {max_departure_city}")

def main():
    # Step 1: Generate flight data
    print("Generating flight data...")
    generate_flight_data()

    # Step 2: Load and process data
    df = load_all_data()
    total_records, dirty_records, top_city_stats, max_arrival_city, max_departure_city = process_data(df)

    # Step 3: Log results
    log_results(total_records, dirty_records, top_city_stats, max_arrival_city, max_departure_city)

if __name__ == "__main__":
    main()