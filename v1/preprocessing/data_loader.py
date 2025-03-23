import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = load_data("../data/hotel_bookings.csv")
    print(df.head())