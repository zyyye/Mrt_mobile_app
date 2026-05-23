from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .stations import load_station_map
from .lta_client import get_fare
from .db import init_db, add_trip

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

station_map = {}

@app.on_event("startup")
def startup_event():
    global station_map
    station_map = load_station_map()
    init_db()

@app.get("/ping")
def ping():
    """Keep-alive endpoint for backend warm-up (prevents cold start)"""
    return {"status": "alive"}

@app.get("/stations")
def get_stations():
    """Return all available stations as a list"""
    if not station_map:
        raise HTTPException(status_code=503, detail="Station data is not available")
    return sorted(list(station_map.keys()))

@app.get("/fare")
def fare(start: str, end: str):
    if not station_map:
        raise HTTPException(status_code=503, detail="Station data is not available")

    if start not in station_map or end not in station_map:
        raise HTTPException(status_code=400, detail="Invalid station selection")

    start_id = station_map[start]
    end_id = station_map[end]

    result = get_fare(start_id, end_id)

    add_trip(start, end, result["fare"], result["distance"])

    return result

@app.get("/")
def home():
    return {
        "message": "MRT Fare API is running",
        "docs": "/docs"
    }