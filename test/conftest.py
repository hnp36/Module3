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
        value1 = Decimal(faker_instance.random_number(digits=2))
        value2 = Decimal(faker_instance.random_number(digits=2)) if _ % 4 != 3 else Decimal(faker_instance.random_number(digits=1))
        operation_key = faker_instance.random_element(elements=list(operation_lookup.keys()))
        operation_func = operation_lookup[operation_key]
        
        if operation_func == division:
            value1 = Decimal('1') if value2 == Decimal('0') else value2
        
        try:
            if operation_func == division and value2== Decimal('0'):
                expected_result = "ZeroDivisionError"
            else:
                expected_result = operation_func(value1, value2)
        except ZeroDivisionError:
            expected_result = "ZeroDivisionError"
        
        yield value1, value2, operation_key, operation_func, expected_result

def pytest_addoption(parser):
    parser.addoption("--record_count", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"value1", "value2", "expected_result"}.intersection(set(metafunc.fixturenames)):
        record_count = metafunc.config.getoption("record_count")
        test_cases = list(create_test_cases(record_count))
        formatted_cases = [(value1, value2, op_key if 'operation_key' in metafunc.fixturenames else op_func, expected) for value1, value2, op_key, op_func, expected in test_cases]
        metafunc.parametrize("value1,value2,operation,expected_result", formatted_cases)
