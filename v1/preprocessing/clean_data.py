import os
import pandas as pd

# Define paths
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "../data")
DATA_PATH = os.path.join(DATA_DIR, "hotel_bookings.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")

os.makedirs(DATA_DIR, exist_ok=True)

def clean_data(df):
    df.fillna({'children': 0, 'agent': 'Unknown', 'company': 'Unknown'}, inplace=True)
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    return df

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    df.to_csv(OUTPUT_PATH, index=False)