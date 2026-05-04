import uuid
from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from src.db.entities import Trip as TripDB
from src.models.trip import Trip as TripModel
from src.services.trip_storage import TripStorage


class TripRepository(TripStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_trip(self, trip: TripModel) -> TripModel:
        db_trip = TripDB(
            id=uuid.uuid4(),
            name=trip.name,
            description=trip.description
        )

        self.db.add(db_trip)
        self.db.commit()
        self.db.refresh(db_trip)

        return TripModel(**db_trip.__dict__)

    def get_trip(self, trip_id: UUID) -> Optional[TripModel]:
        trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()
        return TripModel(**trip.__dict__) if trip else None

    def get_trips(self) -> List[TripModel]:
        return [TripModel(**t.__dict__) for t in self.db.query(TripDB).all()]

    def update_trip(self, trip_id: UUID, trip: TripModel) -> Optional[TripModel]:
        db_trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()

        if not db_trip:
            return None

        db_trip.name = trip.name
        db_trip.description = trip.description

        self.db.commit()
        self.db.refresh(db_trip)

        return trip

    def delete_trip(self, trip_id: UUID) -> bool:
        trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()

        if not trip:
            return False

        self.db.delete(trip)
        self.db.commit()
        return True