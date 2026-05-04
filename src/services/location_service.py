from typing import List
from src.models.location import Location
from src.services.location_storage import LocationStorage


class LocationService(LocationStorage):

    def __init__(self):
        self.locations: List[Location] = []

    def create_location(self, location: Location) -> Location:
        self.locations.append(location)
        return location

    def get_locations(self) -> List[Location]:
        return self.locations