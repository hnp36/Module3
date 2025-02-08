"""My arithmetic operation"""
def addition(first_term, second_term):
    """adding two numbers"""
    return first_term + second_term

def subtraction(minuend, subtrahend):
    """substracting two numbers"""
    return minuend - subtrahend

def multiplication(multiplicand, multiplier):
    """multipling two numbers"""
    return multiplicand * multiplier

def division(dividend, divisor):
    """dividing two numbers and throwing error if divided by 0"""
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    return dividend / divisor
