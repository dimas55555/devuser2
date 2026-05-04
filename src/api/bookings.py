from fastapi import APIRouter, Depends
from typing import List

from src.dependencies.booking_dependency import get_booking_storage
from src.services.booking_storage import BookingStorage
from src.models.booking import Booking

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=Booking)
def create_booking(
    booking: Booking,
    storage: BookingStorage = Depends(get_booking_storage)
):
    return storage.create_booking(booking)


@router.get("/", response_model=List[Booking])
def get_bookings(
    storage: BookingStorage = Depends(get_booking_storage)
):
    return storage.get_bookings()