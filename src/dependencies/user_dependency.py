from fastapi import Depends
from functools import lru_cache
from sqlalchemy.orm import Session

from src.config import get_settings
from src.db.database import get_db
from src.services.user_service import UserService
from src.db.users_repository import UserRepository
from src.services.user_storage import UserStorage

def get_user_storage(db: Session = Depends(get_db)) -> UserStorage:
    """
    Returns:
    - UserService (in-memory) if TEST_MODE = True
    - UserRepository (DB) if TEST_MODE = False
    """

    settings = get_settings()

    if settings.TEST_MODE:
        return UserService()

    return UserRepository(db)