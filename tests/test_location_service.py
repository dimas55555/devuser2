from uuid import uuid4
from src.services.location_service import LocationService
from src.models.location import Location


def test_create_location_in_memory():
    service = LocationService()

    location = Location(
        id=uuid4(),
        trip_id=uuid4(),
        name="Kyiv",
        country="Ukraine",
        city="Kyiv"
    )

    created = service.create_location(location)

    assert created.name == "Kyiv"
    assert len(service.get_locations()) == 1