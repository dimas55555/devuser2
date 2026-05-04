from fastapi import Depends
from sqlalchemy.orm import Session

from src.config import get_settings
from src.db.database import get_db
from src.services.booking_service import BookingService
from src.db.bookings_repository import BookingRepository
from src.services.booking_storage import BookingStorage


def get_booking_storage(db: Session = Depends(get_db)) -> BookingStorage:
    if get_settings().TEST_MODE:
        return BookingService()

    return BookingRepository(db)