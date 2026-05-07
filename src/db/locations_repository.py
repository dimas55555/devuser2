from typing import List, Optional
from sqlalchemy.orm import Session

from src.db.entities import Location as LocationDB
from src.models.location import Location as LocationModel
from src.services.location_storage import LocationStorage


class LocationRepository(LocationStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_location(self, location: LocationModel) -> LocationModel:
        db_location = LocationDB(
            name=location.name,
            trip_id=location.trip_id
        )

        self.db.add(db_location)
        self.db.commit()
        self.db.refresh(db_location)

        return LocationModel(
            id=db_location.id,
            name=db_location.name,
            country=None,  # поки нема в БД
            trip_id=db_location.trip_id
        )

    def get_locations(self) -> List[LocationModel]:
        locations = self.db.query(LocationDB).all()

        return [
            LocationModel(
                id=l.id,
                name=l.name,
                country=None,
                trip_id=l.trip_id
            )
            for l in locations
        ]

    def get_location(self, location_id: int) -> Optional[LocationModel]:
        l = self.db.query(LocationDB).filter(LocationDB.id == location_id).first()

        if not l:
            return None

        return LocationModel(
            id=l.id,
            name=l.name,
            country=None,
            trip_id=l.trip_id
        )

    def delete_location(self, location_id: int) -> bool:
        l = self.db.query(LocationDB).filter(LocationDB.id == location_id).first()

        if not l:
            return False

        self.db.delete(l)
        self.db.commit()
        return True