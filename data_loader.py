import os
import pandas as pd

OUTPUT_DIR = '/tmp/flights'

def load_all_data():
    """Loads all JSON flight data files from /tmp/flights into a single DataFrame for pandas."""
    all_data = []
    # Generate a list of directory paths at /tmp/flights with os.walk
    for root, _, files in os.walk(OUTPUT_DIR): # dirs replaced as we don't have, returns tuples for root and files
        for file_name in files:
            #constructing full path for all json files
            if file_name.endswith('.json'):
                file_path = os.path.join(root, file_name)
                try:
                    data = pd.read_json(file_path)
                    all_data.append(data)
                except ValueError as e:
                    print(f"Error reading {file_path}: {e}")
    if all_data:
        # Concatenate all DataFrames in the list `all_data` into a single DataFrame.
        combined_data = pd.concat(all_data, ignore_index=True)
        return combined_data
    else:
        # If `all_data` is empty (no data was loaded), return an empty DataFrame.
        return pd.DataFrame()