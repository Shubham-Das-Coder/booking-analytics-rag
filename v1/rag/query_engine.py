import os
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "../data/faiss_index.bin")
MAPPINGS_PATH = os.path.join(BASE_DIR, "../data/faiss_mappings.csv")

if not os.path.exists(FAISS_INDEX_PATH) or not os.path.exists(MAPPINGS_PATH):
    raise FileNotFoundError(f"Error: Missing FAISS index or mapping files.")

df = pd.read_csv(MAPPINGS_PATH)
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(FAISS_INDEX_PATH)

def query_booking(question, top_k=10):
    query_embedding = np.array([model.encode(question)], dtype=np.float32)
    distances, indices = index.search(query_embedding, top_k)
    
    results = df.iloc[indices[0]]

    if "total revenue" in question.lower():
        total_revenue = results["adr"].sum()
        return {"Total Revenue": f"${total_revenue:.2f}"}

    return results.to_dict(orient="records")