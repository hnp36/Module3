"""Calculator module providing basic arithmetic operations."""
from decimal import Decimal
from typing import Callable

from calculator.operation import addition, subtraction, multiplication, division
from calculator.calculation import Calculation

class Calculator:
    """MY Calculator class"""

    @staticmethod
    def execute_operation(value1: Decimal, value2: Decimal,
                           operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(value1, value2, operation)
        return calculation.perform()

    @staticmethod
    def perform_addition(value1: Decimal, value2: Decimal) -> Decimal:
        """My Addition"""
        return Calculator.execute_operation(value1, value2, addition)

    @staticmethod
    def perform_subtraction(value1: Decimal, value2: Decimal) -> Decimal:
        """My Substraction"""
        return Calculator.execute_operation(value1, value2, subtraction)

    @staticmethod
    def perform_multiplication(value1: Decimal, value2: Decimal) -> Decimal:
        """My Multiplication"""
        return Calculator.execute_operation(value1, value2, multiplication)

    @staticmethod
    def perform_division(value1: Decimal, value2: Decimal) -> Decimal:
        """My Division"""
        return Calculator.execute_operation(value1, value2, division)
