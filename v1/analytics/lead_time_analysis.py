import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "../data/cleaned_data.csv"))

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Error: Data file not found at {DATA_PATH}")

def lead_time_distribution(df):
    df["lead_time"].plot(kind="hist", bins=50, figsize=(10, 5), title="Lead Time Distribution")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    lead_time_distribution(df)