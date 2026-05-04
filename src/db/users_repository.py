import uuid
from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from src.db.entities import User as UserDB
from src.models.user import User as UserModel
from src.services.user_storage import UserStorage

class UserRepository(UserStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserModel) -> UserModel:
        db_user = UserDB(
            id=uuid.uuid4(),
            name=user.name,
            email=user.email
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return UserModel(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email
        )

    def get_user(self, user_id: UUID) -> Optional[UserModel]:
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()

        if not user:
            return None

        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email
        )

    def get_users(self) -> List[UserModel]:
        users = self.db.query(UserDB).all()

        return [
            UserModel(id=u.id, name=u.name, email=u.email)
            for u in users
        ]

    def update_user(self, user_id: UUID, user: UserModel) -> Optional[UserModel]:
        db_user = self.db.query(UserDB).filter(UserDB.id == user_id).first()

        if not db_user:
            return None

        db_user.name = user.name
        db_user.email = user.email

        self.db.commit()
        self.db.refresh(db_user)

        return user

    def delete_user(self, user_id: UUID) -> bool:
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()

        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True