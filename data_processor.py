import pandas as pd

def process_data(df):
    """Processes the data to filter out dirty records and calculate the statistics."""
    total_records = len(df)
    dirty_records = df.isnull().any(axis=1).sum()
    
    clean_df = df.dropna()
    
    # Calculate average and 95th percentile of flight duration for top destination cities
    top_cities = (
        clean_df.groupby('destination_city')['flight_duration_secs'] #Split data based on destination_city 
        .agg(['mean', lambda x: x.quantile(0.95)]) # mean for average flight duration and 95 percentile for upper range for typical flights 
        .rename(columns={'mean': 'avg_duration', '<lambda>': 'p95_duration'})
        .nlargest(25, 'avg_duration') # top 25 rows based on mean/avg_duration
    )

    passengers_arrived = clean_df.groupby('destination_city')['# of passengers on board'].sum()
    passengers_left = clean_df.groupby('origin_city')['# of passengers on board'].sum()
    
    max_arrival_city = passengers_arrived.idxmax()
    max_departure_city = passengers_left.idxmax()
    
    return total_records, dirty_records, top_cities, max_arrival_city, max_departure_city