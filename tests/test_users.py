from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@test.com"
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["name"] == "Test User"
    assert data["email"] == "test@test.com"


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)