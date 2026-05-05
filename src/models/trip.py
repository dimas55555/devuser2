from pydantic import BaseModel


class Trip(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None
    user_id: int