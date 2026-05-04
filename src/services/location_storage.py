from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.models.location import Location


class LocationStorage(ABC):

    @abstractmethod
    def create_location(self, location: Location) -> Location:
        pass

    @abstractmethod
    def get_locations(self) -> List[Location]:
        pass