"""Calculation class to perform arithmetic operations """
class Calculation:
    """Function that takes two parameters and returns their operation result"""

    def __init__(self, first_number, second_number, operation_function):
        """ Initializing a new calculation"""
        self.first_number = first_number
        self.second_number = second_number
        self.operation_function = operation_function

    def execute_operation(self):
        """Execute the stored operation on the two numbers"""
        return self.operation_function(self.first_number, self.second_number)
