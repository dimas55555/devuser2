from pydantic import BaseModel


class Booking(BaseModel):
    id: int | None = None
    type: str

    user_id: int
    trip_id: int