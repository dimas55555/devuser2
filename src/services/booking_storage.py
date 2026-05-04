from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from src.models.booking import Booking


class BookingStorage(ABC):

    @abstractmethod
    def create_booking(self, booking: Booking) -> Booking:
        pass

    @abstractmethod
    def get_bookings(self) -> List[Booking]:
        pass