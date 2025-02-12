import pytest
import sys
import os
from main import calculate_and_print  # Ensure this import matches your project structure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import calculate_and_print

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("num1_str, num2_str, operation_key, expected_output", [
    ("5", "3", 'addition', "The result of 5 addition 3 is equal to 8"),
    ("10", "2", 'subtraction', "The result of 10 subtraction 2 is equal to 8"),
    ("4", "5", 'multiplication', "The result of 4 multiplication 5 is equal to 20"),
    ("20", "4", 'division', "The result of 20 division 4 is equal to 5"),
    ("1", "0", 'division', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'addition', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtraction', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(num1_str, num2_str, operation_key, expected_output, capsys):
    calculate_and_print(num1_str, num2_str, operation_key)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
