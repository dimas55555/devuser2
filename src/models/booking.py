from pydantic import BaseModel
from uuid import UUID


class Booking(BaseModel):
    id: UUID | None = None
    user_id: UUID
    trip_id: UUID