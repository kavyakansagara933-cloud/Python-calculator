from calculator import add, subtract, multiply, divide, modulus


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(5, 4) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_modulus():
    assert modulus(10, 3) == 1


def test_divide_by_zero():
    assert divide(10, 0) == "Cannot divide by zero"


def test_modulus_by_zero():
    assert modulus(10, 0) == "Cannot divide by zero"

def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_multiply_decimals():
    assert multiply(2.5, 4) == 10