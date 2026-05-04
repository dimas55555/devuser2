from fastapi import Depends
from sqlalchemy.orm import Session

from src.config import get_settings
from src.db.database import get_db
from src.services.location_service import LocationService
from src.db.locations_repository import LocationRepository
from src.services.location_storage import LocationStorage


def get_location_storage(db: Session = Depends(get_db)) -> LocationStorage:
    if get_settings().TEST_MODE:
        return LocationService()

    return LocationRepository(db)