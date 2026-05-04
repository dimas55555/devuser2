from pydantic import BaseModel
from uuid import UUID


class Trip(BaseModel):
    id: UUID | None = None
    title: str
    description: str | None = None
    user_id: UUID