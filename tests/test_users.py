from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    """Тест створення нового користувача"""
    # 1. Надсилаємо POST запит на створення користувача
    response = client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@test.com"
        }
    )

    # 2. Перевіряємо, чи успішний запит (код 200)
    assert response.status_code == 200

    # 3. Перевіряємо дані у відповіді
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test User"
    assert data["email"] == "test@test.com"


def test_get_users():
    """Тест отримання списку користувачів"""
    # 1. Надсилаємо GET запит на отримання всіх користувачів
    response = client.get("/users/")

    # 2. Перевіряємо код відповіді
    assert response.status_code == 200

    # 3. Перевіряємо, чи відповідь є списком (list)
    data = response.json()
    assert isinstance(data, list)