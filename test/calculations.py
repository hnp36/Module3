'''My Calculator Test Suite'''
import pytest
from decimal import Decimal
# Import the required classes and functions from the calculator module.
from calculator.calculation import Calculation

from calculator.operation import addition, subtraction, multiplication, division

# Use pytest.fixture to set up the test environment by preparing necessary data before tests run.
@pytest.fixture
def calculator_setup():
    """Prepare the calculation history by clearing any existing records and adding sample calculations."""
    Calculation.clear_history()
    # Add a few sample calculations to the history for testing purposes.
    Calculation.add_calculation(Calculation(Decimal('12'), Decimal('8'), addition))
    Calculation.add_calculation(Calculation(Decimal('30'), Decimal('5'), subtraction))

def test_add_calculation_to_history(calculator_setup):
    """Verify that adding a new calculation correctly updates the history."""
    new_calculation = Calculation(Decimal('3'), Decimal('7'), addition)
    # Add the new calculation to the history.
    Calculation.add_calculation(new_calculation)
    
    assert Calculation.get_latest_calculation() == new_calculation, "New calculation not added to the history"

def test_fetch_calculation_history(calculator_setup):
    """Fetch the calculation history."""
    history = Calculation.get_all_calculations()
   
    assert len(history) == 2,"The history does not contain the expected number of calculations"

def test_clear_all_calculations(calculator_setup):
    """Clear the history."""
   
    Calculation.clear_history()
    assert len(Calculation.get_all_calculations()) == 0, "History was not cleared successfully"

def test_get_most_recent_calculation(calculator_setup):
    """Fetch the most recent calculation from the history."""
    
    most_recent = Calculation.get_latest_calculation()
    assert most_recent.a == Decimal('30') and most_recent.b == Decimal('5'), "Incorrect latest calculation fetched"

def test_search_by_operation_type(calculator_setup):
    """Test that finding calculations by operation type returns the correct results."""
    
    addition_calculations = Calculation.find_calculations_by_operation("add")
    assert len(addition_calculations) == 1, "Incorrect number of add operations found"
    subtraction_calculations = Calculation.find_calculations_by_operation("subtract")
    assert len(subtraction_calculations) == 1, "Incorrect number of subtract operations found"

def test_get_latest_calculation_when_empty():
    """Clear the calculation history to simulate an empty history."""

    Calculation.clear_history()
    assert Calculation.get_latest_calculation() is None, "Expected None when history is empty"
