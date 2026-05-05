from abc import ABC, abstractmethod
from typing import List, Optional
from src.models.user import User


class UserStorage(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: User) -> Optional[User]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass