from typing import List, Optional
from sqlalchemy.orm import Session

from src.db.entities import Trip as TripDB
from src.models.trip import Trip as TripModel
from src.services.trip_storage import TripStorage


class TripRepository(TripStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_trip(self, trip: TripModel) -> TripModel:
        db_trip = TripDB(
            title=trip.title,
            user_id=trip.user_id
        )

        self.db.add(db_trip)
        self.db.commit()
        self.db.refresh(db_trip)

        return TripModel(
            id=db_trip.id,
            title=db_trip.title,
            user_id=db_trip.user_id
        )

    def get_trip(self, trip_id: int) -> Optional[TripModel]:
        trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()

        if not trip:
            return None

        return TripModel(
            id=trip.id,
            title=trip.title,
            user_id=trip.user_id
        )

    def get_trips(self) -> List[TripModel]:
        trips = self.db.query(TripDB).all()

        return [
            TripModel(
                id=t.id,
                title=t.title,
                user_id=t.user_id
            )
            for t in trips
        ]

    def update_trip(self, trip_id: int, trip: TripModel) -> Optional[TripModel]:
        db_trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()

        if not db_trip:
            return None

        db_trip.title = trip.title
        db_trip.user_id = trip.user_id

        self.db.commit()
        self.db.refresh(db_trip)

        return TripModel(
            id=db_trip.id,
            title=db_trip.title,
            user_id=db_trip.user_id
        )

    def delete_trip(self, trip_id: int) -> bool:
        trip = self.db.query(TripDB).filter(TripDB.id == trip_id).first()

        if not trip:
            return False

        self.db.delete(trip)
        self.db.commit()
        return True