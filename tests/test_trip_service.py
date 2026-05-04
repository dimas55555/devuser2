from datetime import date
from src.services.trip_service import TripService
from src.models.trip import Trip

def test_create_trip():
    service = TripService()
    service.trips = []
    trip = Trip(
        title="Paris Trip",
        description="Trip to Paris",
        start_date=date(2025, 6, 1),
        end_date=date(2025, 6, 10),
        price=1200.0
    )

    created_trip = service.create_trip(trip)
    assert created_trip.title == "Paris Trip"