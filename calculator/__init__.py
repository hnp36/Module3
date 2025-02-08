"""MY Calculator operators"""
from calculator.calculation import Calculation
from calculator.operation import addition, subtraction, multiplication, division

class Calculator:
    """MY Calculator class"""
    @staticmethod
    def perform_addition(value1, value2):
        """My Addition"""
        computation = Calculation(value1, value2, addition)
        return computation.execute_operation()

    @staticmethod
    def perform_subtraction(value1, value2):
        """My Substraction"""
        computation = Calculation(value1, value2, subtraction)
        return computation.execute_operation()

    @staticmethod
    def perform_multiplication(value1, value2):
        """My Multiplication"""
        computation = Calculation(value1, value2, multiplication)
        return computation.execute_operation()

    @staticmethod
    def perform_division(value1, value2):
        """My Division"""
        computation = Calculation(value1, value2, division)
        return computation.execute_operation()
