import pandas as pd
import os
from analytics.revenue_analysis import revenue_trends
from analytics.cancellation_rate import cancellation_rate
from analytics.geo_distribution import geo_distribution
from analytics.lead_time_analysis import lead_time_distribution
from analytics.additional_metrics import average_booking_price
from rag.query_engine import query_booking

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/cleaned_data.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Error: Data file not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

def get_analytics():
    return {
        "Revenue Trends": revenue_trends(df),
        "Cancellation Rate": cancellation_rate(df),
        "Geographical Distribution": geo_distribution(df),
        "Lead Time Distribution": lead_time_distribution(df),
        "Average Booking Price": average_booking_price(df),
    }

def ask_question(query: str):
    return query_booking(query)