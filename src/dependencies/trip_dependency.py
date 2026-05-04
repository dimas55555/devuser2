from fastapi import Depends
from sqlalchemy.orm import Session

from src.config import get_settings
from src.db.database import get_db
from src.services.trip_service import TripService
from src.db.trips_repository import TripRepository
from src.services.trip_storage import TripStorage


def get_trip_storage(db: Session = Depends(get_db)) -> TripStorage:
    if get_settings().TEST_MODE:
        return TripService()

    return TripRepository(db)