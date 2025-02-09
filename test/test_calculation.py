"""Test module for calculation operations and functionality."""
from decimal import Decimal
import pytest
from calculator.operation import addition, subtraction, multiplication, division
from calculator.calculation import Calculation

TEST_PARAMETERS = [
    (Decimal('20'), Decimal('4'), addition, Decimal('24')),
    (Decimal('20'), Decimal('4'), subtraction, Decimal('16')),
    (Decimal('20'), Decimal('4'), multiplication, Decimal('80')),
    (Decimal('20'), Decimal('4'), division, Decimal('5')),
    (Decimal('20.5'), Decimal('0.5'), addition, Decimal('21.0')),
    (Decimal('20.5'), Decimal('0.5'), subtraction, Decimal('20.0')),
    (Decimal('20.5'), Decimal('4'), multiplication, Decimal('82.0')),
    (Decimal('20'), Decimal('0.5'), division, Decimal('40'))
]

@pytest.mark.parametrize(
    "value1, value2, arithmetic_operation, expected_result",
    TEST_PARAMETERS
)
def test_perform_operations(value1, value2, arithmetic_operation, expected_result):
    """Test calculation operations with different inputs."""
    calculation = Calculation(value1, value2, arithmetic_operation)
    assert calculation.execute() == expected_result

def test_calculation_repr_method():
    """Test string representation of Calculation class."""
    calculation = Calculation(Decimal('15'), Decimal('3'), addition)
    expected_repr = "Calculation(15, 3, add)"
    assert repr(calculation) == expected_repr

def test_division_by_zero_error():
    """Test that division by zero raises appropriate error."""
    calculation = Calculation(Decimal('12'), Decimal('0'), division)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.execute()
