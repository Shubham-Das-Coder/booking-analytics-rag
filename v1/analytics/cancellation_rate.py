import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")

if not os.path.exists(CLEANED_DATA_PATH):
    raise FileNotFoundError(f"Error: Data file not found at {CLEANED_DATA_PATH}. Please check the path.")

def cancellation_rate(df):
    cancel_percentage = (df["is_canceled"].sum() / len(df)) * 100
    return f"Cancellation Rate: {cancel_percentage:.2f}%"

if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    print(cancellation_rate(df))