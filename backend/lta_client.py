import requests
from .config import API_URL

TRIP_INFO = (
    "usiAccumulatedDistance1=0-usiAccumulatedDistance2=0-usiAccumulatedDistance3=0-"
    "usiAccumulatedDistance4=0-usiAccumulatedDistance5=0-usiAccumulatedDistance6=0-"
    "usiAccumulatedFare1=0-usiAccumulatedFare2=0-usiAccumulatedFare3=0-"
    "usiAccumulatedFare4=0-usiAccumulatedFare5=0-usiAccumulatedFare6=0"
)

def get_fare(start_id, end_id):
    payload = {
        "fare": 30,
        "from": start_id,
        "to": end_id,
        "tripInfo": TRIP_INFO,
        "addTripInfo": 0
    }

    r = requests.post(API_URL, data=payload)
    data = r.json()

    return {
        "fare": int(data["fare"]) / 100,
        "distance": int(data["distance"]) / 1000
    }