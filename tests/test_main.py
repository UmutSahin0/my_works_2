# tests/test_count.py

from app.main import count_logic

def test_count_up_valid():
    assert count_logic(5) == "12345"

def test_count_up_invalid():
    try:
        count_logic(0)
    except ValueError as e:
        assert str(e) == "Number must be >= 1"
