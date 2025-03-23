import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")

if not os.path.exists(CLEANED_DATA_PATH):
    raise FileNotFoundError(f"Error: Data file not found at {CLEANED_DATA_PATH}. Please check the path.")

def geo_distribution(df):
    country_counts = df["country"].value_counts()
    country_counts.plot(kind='bar', figsize=(12, 6), title="Geographical Distribution of Bookings")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    geo_distribution(df)