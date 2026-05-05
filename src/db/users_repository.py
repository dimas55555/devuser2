from sqlalchemy.orm import Session
from src.db.entities import User
from src.models.user import User as UserModel
from src.services.user_storage import UserStorage


class UserRepository(UserStorage):

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, userModel: UserModel) -> UserModel:
        user = User(
            name=userModel.name,
            email=userModel.email
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email
        )

    def get_users(self):
        users = self.db.query(User).all()
        return [
            UserModel(id=u.id, name=u.name, email=u.email)
            for u in users
        ]

    def get_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        return UserModel(id=user.id, name=user.name, email=user.email)

    def update_user(self, user_id: int, userModel: UserModel):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        user.name = userModel.name
        user.email = userModel.email

        self.db.commit()
        self.db.refresh(user)

        return UserModel(id=user.id, name=user.name, email=user.email)

    def delete_user(self, user_id: int) -> bool:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True