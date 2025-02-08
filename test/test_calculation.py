'''Operations Testing Module'''
from calculator.operation import addition, multiplication, subtraction, division

def test_operation_addition():
    '''Verify addition operation'''    
    result = addition(5, 3)
    assert result == 8

def test_operation_subtraction():
    '''Verify subtraction operation'''    
    result = subtraction(10, 4)
    assert result == 6

def test_operation_multiplication():
    '''Verify multiplication operation'''    
    result = multiplication(5, 5)
    assert result == 25

def test_operation_division():
    '''Verify division operation'''    
    result = division(20, 4)
    assert result == 5
