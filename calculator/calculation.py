# pylint: disable=too-few-public-methods
from decimal import Decimal
from typing import Callable, List
from calculator.operation import addition, subtraction, multiplication, division

class Calculation:
    """Calculation class to perform arithmetic operations"""
    history: List["Calculation"] = []
    
    def __init__(self, value1: Decimal, value2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize the calculation with two values and an operation."""
        self.value1 = value1
        self.value2 = value2
        self.operation = operation

    @staticmethod
    def create(value1: Decimal, value2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> "Calculation":
        """Create a new calculation instance"""
        calculation = Calculation(value1, value2, operation)
        Calculation.history.append(calculation)
        return calculation
    
    def perform(self) -> Decimal:
        """Execute the calculation"""
        return self.operation(self.value1, self.value2)
    
    def execute(self) -> Decimal:
        """Execute the calculation"""
        return self.perform()
    
    def __repr__(self) -> str:
        """Return string representation of the calculation"""
        return f"Calculation({self.value1}, {self.value2}, {self.operation.__name__[:3]})"
    
    @classmethod
    def get_history(cls) -> List["Calculation"]:
        """Get calculation history"""
        return cls.history
    
    @classmethod
    def clear_history(cls) -> None:
        """Clear calculation history"""
        cls.history.clear()
    
    @classmethod
    def get_latest_calculation(cls) -> "Calculation":
        """Get the most recent calculation"""
        return cls.history[-1] if cls.history else None
    
    @classmethod
    def add_calculation(cls, calculation: "Calculation") -> None:
        """Add a calculation to history"""
        cls.history.append(calculation)
    
    @classmethod
    def get_all_calculations(cls) -> List["Calculation"]:
        """Get all calculations"""
        return cls.history
    
    @classmethod
    def find_calculations_by_operation(cls, operation_name: str) -> List["Calculation"]:
        """Find calculations by operation type"""
        return [calc for calc in cls.history if calc.operation.__name__.startswith(operation_name)]
