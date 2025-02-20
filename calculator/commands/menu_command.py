""" MenuCommand Module
This module implements the menu display functionality for the calculator application."""

from calculator.commands.command import Command

# pylint: disable=too-few-public-methods
class MenuCommand(Command):
    """
    This class represents a command to display the calculator menu, 
    listing available operations and commands."""

    def execute(self):
        """Display the calculator menu"""
        print("\nCalculator Menu:")
        print("1. Add (add)")
        print("2. Subtract (subtract)")
        print("3. Multiply (multiply)")
        print("4. Divide (divide)")
        print("5. Help (help)")
        print("6. Exit (exit)\n")
