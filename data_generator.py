import os
import json
from datetime import datetime
from random import randint, choice, random

# Configurations
OUTPUT_DIR = 'C:/tmp/flights'
NUM_FILES = 5000
NUM_CITIES = randint(100, 200)  # Randomly choose between 100 and 200 cities
DURATION_RANGE = (3600, 14400)  # Flight durations between 1 and 4 hours
PASSENGERS_RANGE = (1, 200)  # Passengers per flight
NULL_PROBABILITY = (0.005, 0.001)  # 0.5% to 0.1%

# Generate a set of city names (for example purposes, using "City-1", "City-2", etc.)
CITIES = [f"City-{i}" for i in range(1, NUM_CITIES + 1)]

def generate_flight_data():
    """Generates flight data and writes it to JSON files."""
    folder_name = datetime.now().strftime('%m-%y')
    destination_folder = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    for i in range(NUM_FILES):
        origin_city = choice(CITIES)
        destination_city = choice(CITIES)
        
        # Ensure origin and destination are not the same
        while destination_city == origin_city:
            destination_city = choice(CITIES)
        
        num_flights = randint(50, 100)
        flights = []
        
        for _ in range(num_flights):
            flight_record = {
                'date': datetime.now().isoformat(),
                'origin_city': origin_city,
                'destination_city': destination_city,
                'flight_duration_secs': randint(*DURATION_RANGE),
                '# of passengers on board': randint(*PASSENGERS_RANGE)
            }
            
            # Generate randon value, for each flight, if it is less than NULL_PROBABILITY then add null value to the data
            if random() < choice(NULL_PROBABILITY):
                # Creates a list of keys in flight records and sets the value of any one as Null
                flight_record[choice(list(flight_record.keys()))] = None
            
            flights.append(flight_record)

        
        # File name based on origin and index
        file_path = os.path.join(destination_folder, f'{folder_name}-{origin_city}-flights-{i}.json')
        
        # Write to JSON
        with open(file_path, 'w') as f:
            json.dump(flights, f)
        
        print(f"Generated file: {file_path}")  # Debug info

if __name__ == "__main__":
    generate_flight_data()