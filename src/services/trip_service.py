from typing import List, Optional
from uuid import UUID
from src.models.trip import Trip
from src.services.trip_storage import TripStorage


class TripService(TripStorage):

    def __init__(self):
        self.trips: List[Trip] = []

    def create_trip(self, trip: Trip) -> Trip:
        self.trips.append(trip)
        return trip

    def get_trip(self, trip_id: UUID) -> Optional[Trip]:
        return next((t for t in self.trips if t.id == trip_id), None)

    def get_trips(self) -> List[Trip]:
        return self.trips

    def update_trip(self, trip_id: UUID, trip: Trip) -> Optional[Trip]:
        for i, t in enumerate(self.trips):
            if t.id == trip_id:
                self.trips[i] = trip
                return trip
        return None

    def delete_trip(self, trip_id: UUID) -> bool:
        for i, t in enumerate(self.trips):
            if t.id == trip_id:
                del self.trips[i]
                return True
        return False