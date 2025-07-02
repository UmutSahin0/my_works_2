# tests/test_count.py

from app.main import count_logic,CountRequest

def test_count_up_valid():
    assert count_logic(CountRequest(5)) == "12345"

