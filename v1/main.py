from fastapi import FastAPI, Query
from api.endpoints import get_analytics, ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Booking Analytics RAG API"}

@app.post("/analytics")
def analytics():
    return get_analytics()

@app.post("/ask")
def ask(query: str = Query(..., description="Booking-related question")):
    return ask_question(query)