from src.calculator import add, subtract,multiply


def test_add():
    result = add(10, 5)
    assert result == 15


def test_subtract():
    result = subtract(10, 5)
    assert result == 5

def test_multiply():
	result = multiply (3,4)
	assert result == 12
