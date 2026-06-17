"""
Unit tests for the app/calculation/__init__.py module using pytest.

This test suite covers both positive and negative scenarios for the Calculation
classes and the CalculationFactory. It ensures that calculations execute correctly,
the factory creates appropriate instances, and error handling behaves as expected.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from unittest.mock import patch
from app.operations import Operation
from app.calculation import (
    Calculation,
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)


# ---------------------------------------------------------------------------
# Calculation ABC
# ---------------------------------------------------------------------------

def test_calculation_is_abstract():
    """
    Test that Calculation cannot be instantiated directly.

    AAA Pattern:
    - Arrange: No setup required.
    - Act: Attempt to instantiate Calculation directly.
    - Assert: TypeError is raised.
    """
    # Act / Assert
    with pytest.raises(TypeError):
        Calculation(1.0, 2.0)


def test_calculation_stores_operands():
    """
    Test that a and b are stored correctly on the instance.

    AAA Pattern:
    - Arrange / Act: Create a calculation with known operands.
    - Assert: Verify a and b match what was passed in.
    """
    # Arrange / Act
    calc = AddCalculation(7.0, 3.0)

    # Assert
    assert calc.a == 7.0
    assert calc.b == 3.0


# ---------------------------------------------------------------------------
# String representations
# ---------------------------------------------------------------------------

def test_calculation_repr_add():
    """
    Test that __repr__ returns the expected format for AddCalculation.

    AAA Pattern:
    - Arrange: Create an AddCalculation instance.
    - Act: Call repr() on it.
    - Assert: Output matches expected format including a= and b= labels.
    """
    # Arrange
    calc = AddCalculation(10.0, 5.0)

    # Act
    result = repr(calc)

    # Assert
    assert result == "AddCalculation(a=10.0, b=5.0)"


def test_calculation_repr_subtract():
    """
    Test that __repr__ returns the expected format for SubtractCalculation.

    AAA Pattern:
    - Arrange: Create a SubtractCalculation instance.
    - Act: Call repr() on it.
    - Assert: Output matches expected format.
    """
    # Arrange
    calc = SubtractCalculation(10.0, 5.0)

    # Act
    result = repr(calc)

    # Assert
    assert result == "SubtractCalculation(a=10.0, b=5.0)"


def test_calculation_repr_divide():
    """
    Test that __repr__ returns the expected format for DivideCalculation.

    AAA Pattern:
    - Arrange: Create a DivideCalculation instance.
    - Act: Call repr() on it.
    - Assert: Output matches expected format.
    """
    # Arrange
    calc = DivideCalculation(10.0, 5.0)

    # Act
    result = repr(calc)

    # Assert
    assert result == "DivideCalculation(a=10.0, b=5.0)"


@patch.object(Operation, 'addition', return_value=15.0)
def test_calculation_str_addition(mock_addition):
    """
    Test the __str__ method of AddCalculation.

    AAA Pattern:
    - Arrange: Create an AddCalculation instance with mocked Operation.
    - Act: Call str() on it.
    - Assert: Output matches expected format with class name, operands, and result.
    """
    # Arrange
    calc = AddCalculation(10.0, 5.0)

    # Act
    result = str(calc)

    # Assert
    assert result == "AddCalculation: 10.0 Add 5.0 = 15.0"


@patch.object(Operation, 'subtraction', return_value=5.0)
def test_calculation_str_subtraction(mock_subtraction):
    """
    Test the __str__ method of SubtractCalculation.

    AAA Pattern:
    - Arrange: Create a SubtractCalculation instance with mocked Operation.
    - Act: Call str() on it.
    - Assert: Output matches expected format.
    """
    # Arrange
    calc = SubtractCalculation(10.0, 5.0)

    # Act
    result = str(calc)

    # Assert
    assert result == "SubtractCalculation: 10.0 Subtract 5.0 = 5.0"


@patch.object(Operation, 'multiplication', return_value=50.0)
def test_calculation_str_multiplication(mock_multiplication):
    """
    Test the __str__ method of MultiplyCalculation.

    AAA Pattern:
    - Arrange: Create a MultiplyCalculation instance with mocked Operation.
    - Act: Call str() on it.
    - Assert: Output matches expected format.
    """
    # Arrange
    calc = MultiplyCalculation(10.0, 5.0)

    # Act
    result = str(calc)

    # Assert
    assert result == "MultiplyCalculation: 10.0 Multiply 5.0 = 50.0"


@patch.object(Operation, 'division', return_value=2.0)
def test_calculation_str_division(mock_division):
    """
    Test the __str__ method of DivideCalculation.

    AAA Pattern:
    - Arrange: Create a DivideCalculation instance with mocked Operation.
    - Act: Call str() on it.
    - Assert: Output matches expected format.
    """
    # Arrange
    calc = DivideCalculation(10.0, 5.0)

    # Act
    result = str(calc)

    # Assert
    assert result == "DivideCalculation: 10.0 Divide 5.0 = 2.0"


# ---------------------------------------------------------------------------
# AddCalculation.execute()
# ---------------------------------------------------------------------------

@patch.object(Operation, 'addition')
def test_add_calculation_execute_positive(mock_addition):
    """
    Test AddCalculation.execute() calls Operation.addition with correct operands.

    AAA Pattern:
    - Arrange: Mock Operation.addition and create AddCalculation.
    - Act: Call execute().
    - Assert: Operation.addition was called correctly and result matches.
    """
    # Arrange
    a, b, expected = 10.0, 5.0, 15.0
    mock_addition.return_value = expected
    calc = AddCalculation(a, b)

    # Act
    result = calc.execute()

    # Assert
    mock_addition.assert_called_once_with(a, b)
    assert result == expected


@patch.object(Operation, 'addition')
def test_add_calculation_execute_negative(mock_addition):
    """
    Test that AddCalculation.execute() propagates exceptions from Operation.addition.

    AAA Pattern:
    - Arrange: Mock Operation.addition to raise an exception.
    - Act: Call execute().
    - Assert: Exception propagates with the correct message.
    """
    # Arrange
    mock_addition.side_effect = Exception("Addition error")
    calc = AddCalculation(10.0, 5.0)

    # Act / Assert
    with pytest.raises(Exception) as exc_info:
        calc.execute()
    assert str(exc_info.value) == "Addition error"


# ---------------------------------------------------------------------------
# SubtractCalculation.execute()
# ---------------------------------------------------------------------------

@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_positive(mock_subtraction):
    """
    Test SubtractCalculation.execute() calls Operation.subtraction with correct operands.

    AAA Pattern:
    - Arrange: Mock Operation.subtraction and create SubtractCalculation.
    - Act: Call execute().
    - Assert: Operation.subtraction was called correctly and result matches.
    """
    # Arrange
    a, b, expected = 10.0, 5.0, 5.0
    mock_subtraction.return_value = expected
    calc = SubtractCalculation(a, b)

    # Act
    result = calc.execute()

    # Assert
    mock_subtraction.assert_called_once_with(a, b)
    assert result == expected


@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_negative(mock_subtraction):
    """
    Test that SubtractCalculation.execute() propagates exceptions from Operation.subtraction.

    AAA Pattern:
    - Arrange: Mock Operation.subtraction to raise an exception.
    - Act: Call execute().
    - Assert: Exception propagates with the correct message.
    """
    # Arrange
    mock_subtraction.side_effect = Exception("Subtraction error")
    calc = SubtractCalculation(10.0, 5.0)

    # Act / Assert
    with pytest.raises(Exception) as exc_info:
        calc.execute()
    assert str(exc_info.value) == "Subtraction error"


# ---------------------------------------------------------------------------
# MultiplyCalculation.execute()
# ---------------------------------------------------------------------------

@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_positive(mock_multiplication):
    """
    Test MultiplyCalculation.execute() calls Operation.multiplication with correct operands.

    AAA Pattern:
    - Arrange: Mock Operation.multiplication and create MultiplyCalculation.
    - Act: Call execute().
    - Assert: Operation.multiplication was called correctly and result matches.
    """
    # Arrange
    a, b, expected = 10.0, 5.0, 50.0
    mock_multiplication.return_value = expected
    calc = MultiplyCalculation(a, b)

    # Act
    result = calc.execute()

    # Assert
    mock_multiplication.assert_called_once_with(a, b)
    assert result == expected


@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_negative(mock_multiplication):
    """
    Test that MultiplyCalculation.execute() propagates exceptions from Operation.multiplication.

    AAA Pattern:
    - Arrange: Mock Operation.multiplication to raise an exception.
    - Act: Call execute().
    - Assert: Exception propagates with the correct message.
    """
    # Arrange
    mock_multiplication.side_effect = Exception("Multiplication error")
    calc = MultiplyCalculation(10.0, 5.0)

    # Act / Assert
    with pytest.raises(Exception) as exc_info:
        calc.execute()
    assert str(exc_info.value) == "Multiplication error"


# ---------------------------------------------------------------------------
# DivideCalculation.execute()
# ---------------------------------------------------------------------------

@patch.object(Operation, 'division')
def test_divide_calculation_execute_positive(mock_division):
    """
    Test DivideCalculation.execute() calls Operation.division with correct operands.

    AAA Pattern:
    - Arrange: Mock Operation.division and create DivideCalculation.
    - Act: Call execute().
    - Assert: Operation.division was called correctly and result matches.
    """
    # Arrange
    a, b, expected = 10.0, 5.0, 2.0
    mock_division.return_value = expected
    calc = DivideCalculation(a, b)

    # Act
    result = calc.execute()

    # Assert
    mock_division.assert_called_once_with(a, b)
    assert result == expected


@patch.object(Operation, 'division')
def test_divide_calculation_execute_negative(mock_division):
    """
    Test that DivideCalculation.execute() propagates exceptions from Operation.division.

    AAA Pattern:
    - Arrange: Mock Operation.division to raise an exception.
    - Act: Call execute().
    - Assert: Exception propagates with the correct message.
    """
    # Arrange
    mock_division.side_effect = Exception("Division error")
    calc = DivideCalculation(10.0, 5.0)

    # Act / Assert
    with pytest.raises(Exception) as exc_info:
        calc.execute()
    assert str(exc_info.value) == "Division error"


def test_divide_calculation_execute_division_by_zero():
    """
    Test that DivideCalculation.execute() raises ZeroDivisionError when b is zero.

    AAA Pattern:
    - Arrange: Create a DivideCalculation with b=0.
    - Act: Call execute().
    - Assert: ZeroDivisionError is raised with the correct message.
    """
    # Arrange
    calc = DivideCalculation(10.0, 0.0)

    # Act / Assert
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        calc.execute()


# ---------------------------------------------------------------------------
# CalculationFactory — registration
# ---------------------------------------------------------------------------

def test_factory_registers_known_types():
    """
    Test that the factory has all four expected operation types registered.

    AAA Pattern:
    - Arrange: No setup required.
    - Act: Check the factory's internal registry.
    - Assert: All four keys are present.
    """
    # Act
    registered = CalculationFactory._calculations.keys()

    # Assert
    assert "add" in registered
    assert "subtract" in registered
    assert "multiply" in registered
    assert "divide" in registered


def test_factory_rejects_non_calculation_subclass():
    """
    Test that registering a class that doesn't subclass Calculation raises TypeError.

    AAA Pattern:
    - Arrange: Define a class that does not subclass Calculation.
    - Act: Attempt to register it.
    - Assert: TypeError is raised.
    """
    # Act / Assert
    with pytest.raises(TypeError):
        @CalculationFactory.register_calculation('bad')
        class NotACalculation:
            pass


def test_factory_duplicate_registration_raises():
    """
    Test that registering an already registered type raises ValueError.

    AAA Pattern:
    - Arrange: Use a type that is already registered ('add').
    - Act: Attempt to register it again.
    - Assert: ValueError is raised with the correct message.
    """
    # Act / Assert
    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation('add')
        class AnotherAddCalculation(Calculation):
            def execute(self) -> float:
                return Operation.addition(self.a, self.b)

    assert "Calculation type 'add' is already registered." in str(exc_info.value)


# ---------------------------------------------------------------------------
# CalculationFactory — create_calculation
# ---------------------------------------------------------------------------

def test_factory_creates_add_calculation():
    """
    Test that create_calculation returns an AddCalculation instance.

    AAA Pattern:
    - Arrange: Define operation and operands.
    - Act: Call create_calculation.
    - Assert: Result is an AddCalculation with correct operands.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation('add', 10.0, 5.0)

    # Assert
    assert isinstance(calc, AddCalculation)
    assert calc.a == 10.0
    assert calc.b == 5.0


def test_factory_creates_subtract_calculation():
    """
    Test that create_calculation returns a SubtractCalculation instance.

    AAA Pattern:
    - Arrange: Define operation and operands.
    - Act: Call create_calculation.
    - Assert: Result is a SubtractCalculation with correct operands.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation('subtract', 10.0, 5.0)

    # Assert
    assert isinstance(calc, SubtractCalculation)
    assert calc.a == 10.0
    assert calc.b == 5.0


def test_factory_creates_multiply_calculation():
    """
    Test that create_calculation returns a MultiplyCalculation instance.

    AAA Pattern:
    - Arrange: Define operation and operands.
    - Act: Call create_calculation.
    - Assert: Result is a MultiplyCalculation with correct operands.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation('multiply', 10.0, 5.0)

    # Assert
    assert isinstance(calc, MultiplyCalculation)
    assert calc.a == 10.0
    assert calc.b == 5.0


def test_factory_creates_divide_calculation():
    """
    Test that create_calculation returns a DivideCalculation instance.

    AAA Pattern:
    - Arrange: Define operation and operands.
    - Act: Call create_calculation.
    - Assert: Result is a DivideCalculation with correct operands.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation('divide', 10.0, 5.0)

    # Assert
    assert isinstance(calc, DivideCalculation)
    assert calc.a == 10.0
    assert calc.b == 5.0


def test_factory_is_case_insensitive():
    """
    Test that create_calculation accepts uppercase operation names.

    AAA Pattern:
    - Arrange: Use uppercase operation name.
    - Act: Call create_calculation.
    - Assert: Correct instance is returned without error.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation('ADD', 1.0, 2.0)

    # Assert
    assert isinstance(calc, AddCalculation)


def test_factory_raises_on_unsupported_operation():
    """
    Test that create_calculation raises ValueError for unknown operation types.

    AAA Pattern:
    - Arrange: Use an unregistered operation name.
    - Act: Call create_calculation.
    - Assert: ValueError is raised with the operation name and available types in the message.
    """
    # Act / Assert
    with pytest.raises(ValueError) as exc_info:
        CalculationFactory.create_calculation('modulus', 5.0, 3.0)

    assert "Unsupported calculation type: 'modulus'" in str(exc_info.value)
    assert "Available types:" in str(exc_info.value)


# ---------------------------------------------------------------------------
# Parameterized execute() tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("calc_type, a, b, expected", [
    ('add', 10.0, 5.0, 15.0),
    ('subtract', 10.0, 5.0, 5.0),
    ('multiply', 10.0, 5.0, 50.0),
    ('divide', 10.0, 5.0, 2.0),
])
@patch.object(Operation, 'addition')
@patch.object(Operation, 'subtraction')
@patch.object(Operation, 'multiplication')
@patch.object(Operation, 'division')
def test_calculation_execute_parameterized(
    mock_division, mock_multiplication, mock_subtraction, mock_addition,
    calc_type, a, b, expected
):
    """
    Parameterized test for execute() across all four calculation types.

    AAA Pattern:
    - Arrange: Mock the relevant Operation method for each type.
    - Act: Create the calculation and call execute().
    - Assert: The correct Operation method was called and result matches.
    """
    # Arrange
    mock_map = {
        'add': mock_addition,
        'subtract': mock_subtraction,
        'multiply': mock_multiplication,
        'divide': mock_division,
    }
    mock_map[calc_type].return_value = expected

    # Act
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    result = calc.execute()

    # Assert
    mock_map[calc_type].assert_called_once_with(a, b)
    assert result == expected


# ---------------------------------------------------------------------------
# Parameterized __str__ tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("calc_type, a, b, expected_str", [
    ('add', 10.0, 5.0, "AddCalculation: 10.0 Add 5.0 = 15.0"),
    ('subtract', 10.0, 5.0, "SubtractCalculation: 10.0 Subtract 5.0 = 5.0"),
    ('multiply', 10.0, 5.0, "MultiplyCalculation: 10.0 Multiply 5.0 = 50.0"),
    ('divide', 10.0, 5.0, "DivideCalculation: 10.0 Divide 5.0 = 2.0"),
])
@patch.object(Operation, 'addition', return_value=15.0)
@patch.object(Operation, 'subtraction', return_value=5.0)
@patch.object(Operation, 'multiplication', return_value=50.0)
@patch.object(Operation, 'division', return_value=2.0)
def test_calculation_str_parameterized(
    mock_division, mock_multiplication, mock_subtraction, mock_addition,
    calc_type, a, b, expected_str
):
    """
    Parameterized test for __str__ across all four calculation types.

    AAA Pattern:
    - Arrange: Mock all Operation methods via decorators.
    - Act: Create the calculation and call str() on it.
    - Assert: String representation matches expected format.
    """
    # Arrange / Act
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    result = str(calc)

    # Assert
    assert result == expected_str
