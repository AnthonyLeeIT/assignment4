"""Factory and Base class for calculator operations"""

from abc import ABC, abstractmethod

from app.operations import Operation


class Calculation(ABC):
    """Abstract Base Class"""
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a 
        self.b: float = b  

    @abstractmethod
    def execute(self) -> float:
        pass # pragma: no cover

    def __repr__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
    def __str__(self):
        operation_name = self.__class__.__name__.replace('Calculation', '')
        result = self.execute()
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
    
    
class CalculationFactory:
    """Calculation Factory Method, registers calculation subclasses"""
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            if not issubclass(subclass, Calculation):
                raise TypeError(f"{subclass.__name__} must subclass Calculation.")
            key = calculation_type.lower()
            if key in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[key] = subclass
            return subclass
        return decorator
    
    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        key = calculation_type.lower()
        calculation_class = cls._calculations.get(key)
        if not calculation_class:
            available = ', '.join(cls._calculations.keys())
            raise ValueError(
                f"Unsupported calculation type: '{calculation_type}'. "
                f"Available types: {available}"
            )
        return calculation_class(a, b)
    

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    def execute(self) -> float:
        return Operation.addition(self.a, self.b)
    

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)


@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)


@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    def execute(self) -> float:
        # Before performing division, check if `b` is zero to avoid ZeroDivisionError.
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        # Calls the division method from the Operation module to perform the division.
        return Operation.division(self.a, self.b)