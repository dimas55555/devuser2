import uuid
from typing import List

from sqlalchemy.orm import Session

from src.db.entities import Location as LocationDB
from src.models.location import Location as LocationModel
from src.services.location_storage import LocationStorage


class LocationRepository(LocationStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_location(self, location: LocationModel) -> LocationModel:
        db_location = LocationDB(
            id=uuid.uuid4(),
            name=location.name,
            country=location.country
        )

        self.db.add(db_location)
        self.db.commit()
        self.db.refresh(db_location)

        return LocationModel(**db_location.__dict__)

    def get_locations(self) -> List[LocationModel]:
        return [
            LocationModel(**l.__dict__)
            for l in self.db.query(LocationDB).all()
        ]