from fastapi import APIRouter, Depends
from typing import List

from src.dependencies.location_dependency import get_location_storage
from src.services.location_storage import LocationStorage
from src.models.location import Location

router = APIRouter(prefix="/locations", tags=["locations"])


@router.post("/", response_model=Location)
def create_location(
    location: Location,
    storage: LocationStorage = Depends(get_location_storage)
):
    return storage.create_location(location)


@router.get("/", response_model=List[Location])
def get_locations(
    storage: LocationStorage = Depends(get_location_storage)
):
    return storage.get_locations()