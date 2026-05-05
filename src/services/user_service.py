from typing import List, Optional
from src.models.user import User
from src.services.user_storage import UserStorage


class UserService(UserStorage):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
            cls._instance.users = []
        return cls._instance

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_users(self) -> List[User]:
        return self.users

    def get_user(self, user_id: int) -> Optional[User]:
        return next((u for u in self.users if u.id == user_id), None)

    def update_user(self, user_id: int, user: User) -> Optional[User]:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                self.users[i] = user
                return user
        return None

    def delete_user(self, user_id: int) -> bool:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                del self.users[i]
                return True
        return False