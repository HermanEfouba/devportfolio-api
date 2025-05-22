from fastapi.testclient import TestClient
from app import app  # anciennement 'from main import app'

client = TestClient(app)

def test_create_and_get_profile():
    data = {
        "id": 1,
        "name": "John Doe",
        "bio": "Backend developer",
        "skills": ["Python", "FastAPI"],
        "projects": ["API DevPortfolio"]
    }

    response = client.post("/profiles", json=data)
    assert response.status_code == 200

    response = client.get("/profiles/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
