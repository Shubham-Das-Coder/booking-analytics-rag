import os
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")
FAISS_INDEX_PATH = os.path.join(DATA_DIR, "faiss_index.bin")
MAPPINGS_PATH = os.path.join(DATA_DIR, "faiss_mappings.csv")

os.makedirs(DATA_DIR, exist_ok=True)

def create_faiss_index(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = df.apply(lambda row: f"Booking at {row['hotel']} on {row['arrival_date_year']}-{row['arrival_date_month']}, price: {row['adr']}", axis=1)
    embeddings = model.encode(texts.tolist())

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype=np.float32))

    faiss.write_index(index, FAISS_INDEX_PATH)
    df.to_csv(MAPPINGS_PATH, index=True)

    print(f"FAISS index saved at: {FAISS_INDEX_PATH}")
    print(f"FAISS mappings saved at: {MAPPINGS_PATH}")

if __name__ == "__main__":
    if not os.path.exists(CLEANED_DATA_PATH):
        raise FileNotFoundError(f"Cleaned data file not found: {CLEANED_DATA_PATH}")

    df = pd.read_csv(CLEANED_DATA_PATH)
    create_faiss_index(df)