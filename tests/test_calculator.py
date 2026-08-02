from src.calculator import add, subtract


def test_add():
    result = add(10, 5)
    assert result == 15


def test_subtract():
    result = subtract(10, 5)
    assert result == 5

