from uuid import uuid4
from src.services.location_service import LocationService
from src.models.location import Location

def test_create_location():
    service = LocationService()
    location = Location(
        trip_id=uuid4(),
        name="Kyiv",
        country="Ukraine",
        city="Kyiv"
    )

    created_location = service.create_location(location)
    assert created_location.name == "Kyiv"