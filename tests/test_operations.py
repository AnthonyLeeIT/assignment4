import pytest
from typing import Union
from app.operations import addition, division, multiplication, subtraction

Number = Union[int, float]

#Addition Tests
@pytest.mark.parametrize( 
    "a, b, expected",
    [
        (5, 10, 15),
        (0, 0, 0),
        (-6, 4, -2),
        (5.7, 4.3, 10.0),
        (-5.7, 4.3, -1.4),
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]                                
)

def test_addition(a, b, expected):
    assert addition(a, b) == pytest.approx(expected)

#def test_addition(a, b, expected):
 #   assert addition(a, b) == expected

# def test_addition():
#    assert addition(1,1) == 2


# Subtractions Tests
@pytest.mark.parametrize( 
    "a, b, expected",
    [
        (10, 5, 5),
        (0, 0, 0),
        (-6, 4, -10),
        (5.7, 4.3, 1.4),
        (-5.7, 4.3, -10),
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_zeros",
        "subtract_negative_and_positive_integer",
        "subtract_two_positive_floats",
        "subtract_negative_float_and_positive_float",
    ]                                
)
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == pytest.approx(expected)

# Multiplication Tests
@pytest.mark.parametrize( 
    "a, b, expected",
    [
        (5, 10, 15),
        (0, 0, 0),
        (-6, 4, -2),
        (5.7, 4.3, 10.0),
        (-5.7, 4.3, -1.4),
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]                                
)
def test_multiplication():
    assert multiplication(1,1) == 1

# Division positive tests
@pytest.mark.parametrize( 
    "a, b, expected",
    [
        (5, 10, 15),
        (0, 0, 0),
        (-6, 4, -2),
        (5.7, 4.3, 10.0),
        (-5.7, 4.3, -1.4),
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]                                
)
def test_division_positive():
    assert division(1,1) == 1

# Division by zero tests

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)