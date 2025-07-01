from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_count_up_valid():
    response = client.post("/count", json={"number": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "123"}

def test_count_up_invalid():
    response = client.post("/count", json={"number": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Number must be >= 1"
