from typing import List, Optional
from uuid import UUID

from src.models.user import User
from src.services.user_storage import UserStorage


class UserService(UserStorage):

    def __init__(self):
        self.users: List[User] = []

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_user(self, user_id: UUID) -> Optional[User]:
        return next((u for u in self.users if u.id == user_id), None)

    def get_users(self) -> List[User]:
        return self.users

    def update_user(self, user_id: UUID, user: User) -> Optional[User]:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                self.users[i] = user
                return user
        return None

    def delete_user(self, user_id: UUID) -> bool:
        for i, u in enumerate(self.users):
            if u.id == user_id:
                del self.users[i]
                return True
        return False