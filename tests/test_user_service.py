from src.services.user_service import UserService
from src.models.user import User

def test_create_user():
    service = UserService()
    service.users = []
    user = User(
        name="TestUser",
        email="test@example.com",
        password="123456"
    )
    created_user = service.create_user(user)
    assert created_user.name == "TestUser"