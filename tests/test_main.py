from fastapi.testclient import TestClient
from app.main import count_up, CountRequest



def test_count_up_valid():
    request = CountRequest(number=5)
    response = count_up(request)
    assert response == {"result": "12345"}