from pydantic import BaseModel


class Location(BaseModel):
    id: int | None = None
    name: str
    trip_id: int