from pydantic import BaseModel


class Location(BaseModel):
    id: int | None = None
    name: str
    country: str | None = None
    trip_id: int