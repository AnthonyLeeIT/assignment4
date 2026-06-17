"""
This test module contains unit tests for the 'app/calculator.py' module.
Each test demonstrates good testing practices using the Arrange-Act-Assert (AAA) pattern.
"""

import pytest
from app.calculation import CalculationFactory
from app.calculator import display_help, display_history, calculator


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def run_calculator(monkeypatch, capsys, inputs):
    """
    Simulates user input and captures output from the calculator REPL.

    :param monkeypatch: pytest fixture to simulate user input
    :param capsys: pytest fixture to capture stdout/stderr
    :param inputs: list of input strings to simulate
    :return: captured stdout as a string
    """
    input_iterator = iter(inputs)

    def mock_input(_):
        try:
            return next(input_iterator)
        except StopIteration:
            raise EOFError()

    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit):
        calculator()
    return capsys.readouterr().out


# ---------------------------------------------------------------------------
# display_help
# ---------------------------------------------------------------------------

def test_display_help(capsys):
    """
    Test that display_help prints all expected sections.

    AAA Pattern:
    - Arrange: No setup required.
    - Act: Call display_help.
    - Assert: Verify key sections appear in the output.
    """
    # Act
    display_help()

    # Assert
    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "help" in captured.out
    assert "history" in captured.out
    assert "exit" in captured.out


# ---------------------------------------------------------------------------
# display_history
# ---------------------------------------------------------------------------

def test_display_history_empty(capsys):
    """
    Test display_history with an empty history list.

    AAA Pattern:
    - Arrange: Create an empty history list.
    - Act: Call display_history.
    - Assert: Verify the empty-history message is shown.
    """
    # Arrange
    history = []

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."


def test_display_history_with_entries(capsys):
    """
    Test display_history with populated (Calculation, result) tuple entries.

    AAA Pattern:
    - Arrange: Build a history list of (Calculation, result) tuples via the factory.
    - Act: Call display_history.
    - Assert: Verify each entry is numbered and formatted correctly.
    """
    # Arrange
    history = [
        (CalculationFactory.create_calculation("add", 10.0, 5.0), 15.0),
        (CalculationFactory.create_calculation("subtract", 20.0, 3.0), 17.0),
        (CalculationFactory.create_calculation("multiply", 7.0, 8.0), 56.0),
        (CalculationFactory.create_calculation("divide", 20.0, 4.0), 5.0),
    ]

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out
    assert "3. MultiplyCalculation: 7.0 Multiply 8.0 = 56.0" in captured.out
    assert "4. DivideCalculation: 20.0 Divide 4.0 = 5.0" in captured.out


# ---------------------------------------------------------------------------
# Special commands
# ---------------------------------------------------------------------------

def test_calculator_exit(monkeypatch, capsys):
    """
    Test that typing 'exit' exits gracefully with code 0.

    AAA Pattern:
    - Arrange: Provide 'exit' as the only input.
    - Act: Run the calculator.
    - Assert: Exit message is shown and exit code is 0.
    """
    # Arrange / Act
    with pytest.raises(SystemExit) as exc_info:
        run_calculator(monkeypatch, capsys, ["exit"])

    # Assert
    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0


def test_calculator_help_command(monkeypatch, capsys):
    """
    Test that typing 'help' displays the help message.

    AAA Pattern:
    - Arrange: Provide 'help' then 'exit'.
    - Act: Run the calculator.
    - Assert: Help header and exit message both appear in output.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["help", "exit"])

    # Assert
    assert "Calculator REPL Help" in output
    assert "Exiting calculator. Goodbye!" in output


def test_calculator_history_command(monkeypatch, capsys):
    """
    Test that typing 'history' after calculations shows a numbered history.

    AAA Pattern:
    - Arrange: Perform two calculations then request history.
    - Act: Run the calculator.
    - Assert: History header and both entries appear in output.
    """
    # Arrange / Act
    output = run_calculator(
        monkeypatch, capsys,
        ["add 10 5", "subtract 20 3", "history", "exit"]
    )

    # Assert
    assert "Calculation History:" in output
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in output
    assert "2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in output


# ---------------------------------------------------------------------------
# Arithmetic operations
# ---------------------------------------------------------------------------

def test_calculator_addition(monkeypatch, capsys):
    """
    Test the addition operation produces the correct result.

    AAA Pattern:
    - Arrange: Provide 'add 10 5'.
    - Act: Run the calculator.
    - Assert: Result line contains 15.0.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["add 10 5", "exit"])

    # Assert
    assert "Result: AddCalculation: 10.0 Add 5.0 = 15.0" in output


def test_calculator_subtraction(monkeypatch, capsys):
    """
    Test the subtraction operation produces the correct result.

    AAA Pattern:
    - Arrange: Provide 'subtract 20 5'.
    - Act: Run the calculator.
    - Assert: Result line matches the expected repr format.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["subtract 20 5", "exit"])

    # Assert
    assert "Result: SubtractCalculation: 20.0 Subtract 5.0 = 15.0" in output


def test_calculator_multiplication(monkeypatch, capsys):
    """
    Test the multiplication operation produces the correct result.

    AAA Pattern:
    - Arrange: Provide 'multiply 7 8'.
    - Act: Run the calculator.
    - Assert: Result line matches the expected repr format.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["multiply 7 8", "exit"])

    # Assert
    assert "Result: MultiplyCalculation: 7.0 Multiply 8.0 = 56.0" in output


def test_calculator_division(monkeypatch, capsys):
    """
    Test the division operation produces the correct result.

    AAA Pattern:
    - Arrange: Provide 'divide 20 4'.
    - Act: Run the calculator.
    - Assert: Result line matches the expected repr format.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["divide 20 4", "exit"])

    # Assert
    assert "Result: DivideCalculation: 20.0 Divide 4.0 = 5.0" in output


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_calculator_division_by_zero(monkeypatch, capsys):
    """
    Test that dividing by zero shows the appropriate error message.

    AAA Pattern:
    - Arrange: Provide 'divide 10 0'.
    - Act: Run the calculator.
    - Assert: Division by zero message appears.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["divide 10 0", "exit"])

    # Assert
    assert "Cannot divide by zero." in output


def test_calculator_invalid_input_format(monkeypatch, capsys):
    """
    Test that malformed input (wrong number of tokens) shows the error message.

    AAA Pattern:
    - Arrange: Provide inputs with too few tokens.
    - Act: Run the calculator.
    - Assert: Invalid input message and help prompt appear.
    """
    # Arrange / Act
    output = run_calculator(
        monkeypatch, capsys,
        ["invalid input", "add 5", "subtract", "exit"]
    )

    # Assert
    assert "Expected format: <operation> <num1> <num2>" in output
    assert "Type 'help' for more information." in output


def test_calculator_invalid_number_input(monkeypatch, capsys):
    """
    Test that non-numeric operands show the invalid input error message.

    AAA Pattern:
    - Arrange: Provide 'add ten five'.
    - Act: Run the calculator.
    - Assert: Invalid input message appears.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["add ten five", "exit"])

    # Assert
    assert "Expected format: <operation> <num1> <num2>" in output


def test_calculator_unsupported_operation(monkeypatch, capsys):
    """
    Test that an unregistered operation shows the unsupported type error.

    AAA Pattern:
    - Arrange: Provide 'modulus 2 3'.
    - Act: Run the calculator.
    - Assert: Unsupported operation message and available types appear.
    """
    # Arrange / Act
    output = run_calculator(monkeypatch, capsys, ["modulus 2 3", "exit"])

    # Assert
    assert "Unsupported calculation type: 'modulus'" in output
    assert "Available types:" in output


def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test that an unexpected exception during execute() shows the generic error message.

    AAA Pattern:
    - Arrange: Mock CalculationFactory to return a calculation whose execute() raises.
    - Act: Run the calculator.
    - Assert: Generic unexpected error message appears.
    """
    # Arrange
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __repr__(self):
            return "MockCalculation"
        def __str__(self):
            return "MockCalculation"

    monkeypatch.setattr(
        'app.calculation.CalculationFactory.create_calculation',
        lambda op, a, b: MockCalculation()
    )

    # Act
    output = run_calculator(monkeypatch, capsys, ["add 10 5", "exit"])

    # Assert
    assert "An unexpected error occurred" in output
    assert "Mock exception during execution" in output


# ---------------------------------------------------------------------------
# Interrupt handling
# ---------------------------------------------------------------------------

def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test that KeyboardInterrupt exits gracefully with code 0.

    AAA Pattern:
    - Arrange: Mock input() to raise KeyboardInterrupt.
    - Act: Run the calculator.
    - Assert: Interrupt message is shown and exit code is 0.
    """
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: (_ for _ in ()).throw(KeyboardInterrupt()))

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Keyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0


def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test that EOFError exits gracefully with code 0.

    AAA Pattern:
    - Arrange: Mock input() to raise EOFError.
    - Act: Run the calculator.
    - Assert: EOF message is shown and exit code is 0.
    """
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: (_ for _ in ()).throw(EOFError()))

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "EOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0
