from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.models.trip import Trip


class TripStorage(ABC):

    @abstractmethod
    def create_trip(self, trip: Trip) -> Trip:
        pass

    @abstractmethod
    def get_trip(self, trip_id: UUID) -> Optional[Trip]:
        pass

    @abstractmethod
    def get_trips(self) -> List[Trip]:
        pass

    @abstractmethod
    def update_trip(self, trip_id: UUID, trip: Trip) -> Optional[Trip]:
        pass

    @abstractmethod
    def delete_trip(self, trip_id: UUID) -> bool:
        pass