from typing import List
from src.models.booking import Booking
from src.services.booking_storage import BookingStorage


class BookingService(BookingStorage):

    def __init__(self):
        self.bookings: List[Booking] = []

    def create_booking(self, booking: Booking) -> Booking:
        self.bookings.append(booking)
        return booking

    def get_bookings(self) -> List[Booking]:
        return self.bookings