from fastapi import APIRouter, Depends
from typing import List

from src.dependencies.trip_dependency import get_trip_storage
from src.services.trip_storage import TripStorage
from src.models.trip import Trip

router = APIRouter(prefix="/trips", tags=["trips"])


@router.post("/", response_model=Trip)
def create_trip(
    trip: Trip,
    storage: TripStorage = Depends(get_trip_storage)
):
    return storage.create_trip(trip)


@router.get("/", response_model=List[Trip])
def get_trips(
    storage: TripStorage = Depends(get_trip_storage)
):
    return storage.get_trips()


@router.get("/{trip_id}", response_model=Trip)
def get_trip(
    trip_id: str,
    storage: TripStorage = Depends(get_trip_storage)
):
    return storage.get_trip(trip_id)


@router.delete("/{trip_id}")
def delete_trip(
    trip_id: str,
    storage: TripStorage = Depends(get_trip_storage)
):
    return storage.delete_trip(trip_id)