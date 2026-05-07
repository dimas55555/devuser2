from typing import List, Optional
from sqlalchemy.orm import Session

from src.db.entities import Booking as BookingDB
from src.models.booking import Booking as BookingModel
from src.services.booking_storage import BookingStorage


class BookingRepository(BookingStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, booking: BookingModel) -> BookingModel:
        db_booking = BookingDB(
            type=booking.type,
            user_id=booking.user_id,
            trip_id=booking.trip_id
        )

        self.db.add(db_booking)
        self.db.commit()
        self.db.refresh(db_booking)

        return BookingModel(
            id=db_booking.id,
            type=db_booking.type,
            user_id=db_booking.user_id,
            trip_id=db_booking.trip_id
        )

    def get_bookings(self) -> List[BookingModel]:
        bookings = self.db.query(BookingDB).all()

        return [
            BookingModel(
                id=b.id,
                type=b.type,
                user_id=b.user_id,
                trip_id=b.trip_id
            )
            for b in bookings
        ]

    def get_booking(self, booking_id: int) -> Optional[BookingModel]:
        b = self.db.query(BookingDB).filter(BookingDB.id == booking_id).first()

        if not b:
            return None

        return BookingModel(
            id=b.id,
            type=b.type,
            user_id=b.user_id,
            trip_id=b.trip_id
        )

    def delete_booking(self, booking_id: int) -> bool:
        b = self.db.query(BookingDB).filter(BookingDB.id == booking_id).first()

        if not b:
            return False

        self.db.delete(b)
        self.db.commit()
        return True