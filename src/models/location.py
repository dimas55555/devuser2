from pydantic import BaseModel
from uuid import UUID


class Location(BaseModel):
    id: UUID | None = None
    name: str
    country: str | None = None