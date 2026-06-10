import pytest
from typing import Union
from app.operations import addition, division, multiplication, subtraction

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
        (-5.7, 4.3, -10.0),
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
        (5, 10, 50),
        (0, 0, 0),
        (-6, 4, -24),
        (5.7, 4.3, 24.51),
        (-5.7, 4.3, -24.51),
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_two_zeros",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
    ]                                
)
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == pytest.approx(expected)

# Division positive tests
@pytest.mark.parametrize( 
    "a, b, expected",
    [
        (10, 5, 2),
        (-10, -5, 2),
        (-24, 6, -4),
        (10.0, 5.0, 2.0),
        (-10.0, 5.0, -2.0),
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_negative_and_positive_integers",
        "divide_two_positive_floats",
        "divide_negative_float_and_positive_float",
    ]                                
)
def test_division(a, b, expected):
    assert division(a, b) == pytest.approx(expected)

# Division by zero tests

@pytest.mark.parametrize(
    "a, b",
    [
        (10, 0),
        (-10, 0),
        (0, 0),
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)