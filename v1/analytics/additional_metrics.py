import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "../data/cleaned_data.csv"))

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Error: Data file not found at {DATA_PATH}")

def average_booking_price(df):
    avg_price = df["adr"].mean()
    return f"Average Booking Price: {avg_price:.2f}"

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    print(average_booking_price(df))