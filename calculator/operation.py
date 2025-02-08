"""My arithmetic operation"""
def addition(first_term, second_term):
    """adding two numbers"""
    return first_term + second_term

def subtraction(first_term, second_term):
    """substracting two numbers"""
    return first_term - second_term

def multiplication(first_term, second_term):
    """multipling two numbers"""
    return first_term * second_term

def division(first_term, second_term):
    """dividing two numbers and throwing error if divided by 0"""
    if second_term == 0:
        raise ValueError("Division by zero is not allowed")
    return first_term / second_term
