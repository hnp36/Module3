import pytest
from decimal import Decimal
from calculator.operation import addition, subtraction, multiplication, division
from calculator.calculation import Calculation

@pytest.mark.parametrize("value1, value2, arithmetic_operation, expected_result", [
    (Decimal('20'), Decimal('4'), addition, Decimal('24')),  # Test addition
    (Decimal('20'), Decimal('4'), subtraction, Decimal('16')),  # Test subtraction
    (Decimal('20'), Decimal('4'), multiplication, Decimal('80')),  # Test multiplication
    (Decimal('20'), Decimal('4'), division, Decimal('5')),  # Test division
    (Decimal('20.5'), Decimal('0.5'), addition, Decimal('21.0')),  # Test addition with decimals
    (Decimal('20.5'), Decimal('0.5'), subtraction, Decimal('20.0')),  # Test subtraction with decimals
    (Decimal('20.5'), Decimal('4'), multiplication, Decimal('82.0')),  # Test multiplication with decimals
    (Decimal('20'), Decimal('0.5'), division, Decimal('40')),  # Test division with decimals
])
def test_perform_operations(value1, value2, arithmetic_operation, expected_result):
    """ Test the functionality of the `Calculation` class with different arithmetic operations."""
    calc_instance = Calculation(value1, value2, arithmetic_operation)  
    assert calc_instance.execute() == expected_result, f"Test failed for {arithmetic_operation.__name__} with {value1} and {value2}"

def test_calculation_repr_method():
    """ Verify the string representation (__repr__) of the `Calculation` class."""
    calc_instance = Calculation(Decimal('15'), Decimal('3'), addition) 
    expected_string_rep = "Calculation(15, 3, add)"  
    assert calc_instance.__repr__() == expected_string_rep, "The __repr__ method output does not match the expected string."

def test_division_by_zero_error():
    """ Ensure that a division by zero raises a ValueError. """
    calc_instance = Calculation(Decimal('12'), Decimal('0'), division)  # Attempt to divide by zero.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  
        calc_instance.execute() 
