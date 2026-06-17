""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

import sys
from typing import List
import readline
from app.operations import addition, subtraction, multiplication, division

INVALID_INPUT_MSG = (
    "Invalid input. Expected format: <operation> <num1> <num2>\n"
    "Type 'help' for more information."
)
DIVIDE_BY_ZERO_MSG = "Cannot divide by zero. Please enter a non-zero divisor."
UNEXPECTED_ERROR_MSG = "An unexpected error occurred: {error}"


def exit_calculator(message: str = "Exiting calculator. Goodbye!") -> None:
    print(f"\n{message}\n")
    sys.exit(0)


def parse_input(user_input: str) -> tuple:
    parts = user_input.lower().split()
    if len(parts) != 3:
        raise ValueError("Expected exactly three tokens: <operation> <num1> <num2>")
    operation, num1_str, num2_str = parts
    return operation, float(num1_str), float(num2_str)


def display_help() -> None:
    """Displays usage instructions and supported operations."""
    print("""
        Calculator REPL Help
        --------------------
        Usage:
            <operation> <number1> <number2>
            - Perform a calculation with the specified operation and two numbers.
        Supported operations:
            add       : Adds two numbers.
            subtract  : Subtracts the second number from the first.
            multiply  : Multiplies two numbers.
            divide    : Divides the first number by the second.

        Special Commands:
            help      : Display this help message.
            history   : Show the history of calculations.
            exit      : Exit the calculator.

        Examples:
            add 1 2
            subtract 11.5 1.5
            multiply 11 7
            divide 100 20
            """)


def display_history(history: List[tuple]) -> None:
    """Displays the history of calculations performed this session."""
    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, (calculation, result) in enumerate(history, start=1):
            print(f"{idx}. {calculation} = {result}")


def calculator() -> None:
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    history: List[tuple] = []

    print("Welcome to the calculator REPL! Type 'help' for instructions or 'exit' to quit.\n")

    while True:
        try:
            user_input: str = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ").strip()

            if not user_input:  # pragma: no cover
                continue

            commands = {
                "help": lambda: display_help(),
                "history": lambda: display_history(history),
                "exit": lambda: exit_calculator(),
            }

            if user_input.lower() in commands:
                commands[user_input.lower()]()
                continue

            try:
                operation, num1, num2 = parse_input(user_input)
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
                result = calculation.execute()
            except ValueError as e:
                print(f"Error: {e}\n{INVALID_INPUT_MSG}")
                continue
            except ZeroDivisionError:
                print(DIVIDE_BY_ZERO_MSG)
                continue
            except Exception as e:
                print(UNEXPECTED_ERROR_MSG.format(error=e))
                continue

            print(f"Result: {calculation} = {result}\n")
            history.append((calculation, result))

        except KeyboardInterrupt:
            exit_calculator("Keyboard interrupt detected. Exiting calculator. Goodbye!")
        except EOFError:
            exit_calculator("EOF detected. Exiting calculator. Goodbye!")


if __name__ == "__main__":
    calculator()  # pragma: no cover