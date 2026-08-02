import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    result = add(10, 5)
    assert result == 15


def test_subtract():
    result = subtract(10, 5)
    assert result == 5

def test_multiply():
	result = multiply (3,4)
	assert result == 12

def test_divide():
    assert divide(10, 2) == 999  # Intentionally failing to test CI
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
