from pydantic import BaseModel
from typing import Optional


class Trip(BaseModel):
    id: int | None = None
    title: str
    user_id: int