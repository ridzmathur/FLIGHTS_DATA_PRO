# FLIGHTS_DATA_PRO
FLIGHTS_DATA_PRO generates random flight data and performs data analysis to extract flight duration statistics and passenger counts between cities.

Project Structure
main.py - The main entry point to generate and analyze flight data.
data_generator.py - Creates random flight data and saves it as JSON files in a structured directory.
data_loader.py - Loads generated JSON files into a single DataFrame.
analyzer.py - Performs data analysis on loaded data, providing insights like average flight duration and total passenger movement.

Prerequisites
Python 3.8+
Pandas library listed in requirements.txt

To install dependencies, run the following command:
pip install -r requirements.txt

To run the project execute main.py
python main.py

Output:
Total records processed
Total dirty records
Top cities by Flight Duration
City with Max Passengers arrived and departed
