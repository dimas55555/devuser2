import uuid
from typing import List

from sqlalchemy.orm import Session

from src.db.entities import Booking as BookingDB
from src.models.booking import Booking as BookingModel
from src.services.booking_storage import BookingStorage


class BookingRepository(BookingStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, booking: BookingModel) -> BookingModel:
        db_booking = BookingDB(
            id=uuid.uuid4(),
            name=booking.name
        )

        self.db.add(db_booking)
        self.db.commit()
        self.db.refresh(db_booking)

        return BookingModel(**db_booking.__dict__)

    def get_bookings(self) -> List[BookingModel]:
        return [
            BookingModel(**b.__dict__)
            for b in self.db.query(BookingDB).all()
        ]