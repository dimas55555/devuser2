from fastapi import APIRouter, Depends
from typing import List

from src.dependencies.user_dependency import get_user_storage
from src.services.user_storage import UserStorage
from src.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User)
def create_user(
    user: User,
    storage: UserStorage = Depends(get_user_storage)
):
    return storage.create_user(user)


@router.get("/", response_model=List[User])
def get_users(
    storage: UserStorage = Depends(get_user_storage)
):
    return storage.get_users()


@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: str,
    storage: UserStorage = Depends(get_user_storage)
):
    return storage.get_user(user_id)


@router.delete("/{user_id}")
def delete_user(
    user_id: str,
    storage: UserStorage = Depends(get_user_storage)
):
    return storage.delete_user(user_id)