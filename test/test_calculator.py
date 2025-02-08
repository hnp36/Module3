'''Advanced Calculator Testing Module'''
from calculator import Calculator

def test_calculator_addition():
    '''Test the static addition method of Calculator'''    
    result = Calculator.perform_addition(3, 4)
    assert result == 7

def test_calculator_subtraction():
    '''Test the static subtraction method of Calculator'''    
    result = Calculator.perform_subtraction(8, 3)
    assert result == 5

def test_calculator_multiplication():
    '''Test the static multiplication method of Calculator'''    
    result = Calculator.perform_multiplication(6, 7)
    assert result == 42

def test_calculator_division():
    '''Test the static division method of Calculator'''    
    result = Calculator.perform_division(15, 3)
    assert result == 5
