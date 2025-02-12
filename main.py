import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def perform_calculation(num1_str, num2_str, operation_key):
    operation_lookup = {
        'addition': Calculator.add,
        'subtraction': Calculator.subtract,
        'multiplication': Calculator.multiply,
        'division': Calculator.divide
    }
    
    try:
        num1_dec, num2_dec = map(Decimal, [num1_str, num2_str])
        operation_func = operation_lookup.get(operation_key)
        if operation_func:
            print(f"The result of {num1_str} {operation_key} {num2_str} is equal to {operation_func(num1_dec, num2_dec)}")
        else:
            print(f"Unknown operation: {operation_key}")
    except InvalidOperation:
        print(f"Invalid number input: {num1_str} or {num2_str} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def execute():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, num1, num2, operation = sys.argv
    perform_calculation(num1, num2, operation)

if __name__ == '__main__':
    execute()
