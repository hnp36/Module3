'''Advanced Calculator Testing Module'''
import pytest
from decimal import Decimal
from calculator import Calculator
from calculator.operation import addition, subtraction, multiplication, division

def test_calculator_addition():
    '''Test the static addition method of Calculator'''    
    result = Calculator.perform_addition(Decimal('3'), Decimal('4'))
    assert result == Decimal('7')

def test_calculator_subtraction():
    '''Test the static subtraction method of Calculator'''    
    result = Calculator.perform_subtraction(Decimal('8'), Decimal('3'))
    assert result == Decimal('5')

def test_calculator_multiplication():
    '''Test the static multiplication method of Calculator'''    
    result = Calculator.perform_multiplication(Decimal('6'), Decimal('7'))
    assert result == Decimal('42')

def test_calculator_division():
    '''Test the static division method of Calculator'''    
    result = Calculator.perform_division(Decimal('15'), Decimal('3'))
    assert result ==Decimal('5')

def test_calculator_division_by_zero():
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError):
        Calculator.perform_division(Decimal('15'), Decimal('0'))
