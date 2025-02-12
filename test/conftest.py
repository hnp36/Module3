import pytest
from decimal import Decimal
from faker import Faker
from calculator.operation import addition, subtraction, multiplication, division

faker_instance = Faker()

def create_test_cases(record_count):
    operation_lookup = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }
    
    for _ in range(record_count):
        num1 = Decimal(faker_instance.random_number(digits=2))
        num2 = Decimal(faker_instance.random_number(digits=2)) if _ % 4 != 3 else Decimal(faker_instance.random_number(digits=1))
        operation_key = faker_instance.random_element(elements=list(operation_lookup.keys()))
        operation_func = operation_lookup[operation_key]
        
        if operation_func == division:
            num2 = Decimal('1') if num2 == Decimal('0') else num2
        
        try:
            if operation_func == division and num2 == Decimal('0'):
                expected_result = "ZeroDivisionError"
            else:
                expected_result = operation_func(num1, num2)
        except ZeroDivisionError:
            expected_result = "ZeroDivisionError"
        
        yield num1, num2, operation_key, operation_func, expected_result

def pytest_addoption(parser):
    parser.addoption("--record_count", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"num1", "num2", "expected_result"}.intersection(set(metafunc.fixturenames)):
        record_count = metafunc.config.getoption("record_count")
        test_cases = list(create_test_cases(record_count))
        formatted_cases = [(num1, num2, op_key if 'operation_key' in metafunc.fixturenames else op_func, expected) for num1, num2, op_key, op_func, expected in test_cases]
        metafunc.parametrize("num1,num2,operation,expected_result", formatted_cases)
