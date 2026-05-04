from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    id: UUID | None = None
    first_name: str
    last_name: str