import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")

if not os.path.exists(CLEANED_DATA_PATH):
    raise FileNotFoundError(f"Cleaned data file not found: {CLEANED_DATA_PATH}")

def revenue_trends(df):
    df['month_year'] = df['arrival_date_month'] + "-" + df['arrival_date_year'].astype(str)
    revenue_data = df.groupby("month_year")["adr"].sum()
    revenue_data.plot(kind='line', figsize=(10, 5), title="Revenue Trends Over Time")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    revenue_trends(df)