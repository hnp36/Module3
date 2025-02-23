"""
CommandHandler Module

This module defines the CommandHandler class, which dynamically loads and executes commands
from the plugins folder. It supports registering commands, executing them, and handling
special commands like 'exit' and 'help'."""
import sys
import importlib
import pkgutil
import inspect
import calculator.plugins  # Import the plugins package
from ..plugins.addition import AdditionCommand
from ..plugins.substraction import SubtractionCommand
from ..plugins.multiplication import MultiplicationCommand
from ..plugins.division import DivisionCommand
from ..plugins.menu_command import MenuCommand

class CommandHandler:
    """CommandHandler dynamically loads and executes commands from the plugins folder."""

    def __init__(self):
        """Initializes the command registry and loads available plugins."""
        self.commands = {}
        self.load_plugins()

    def load_plugins(self):
        """Dynamically load command classes from the plugins folder."""
        package = calculator.plugins  # The plugin package
        for _, module_name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            module = importlib.import_module(module_name)  # Import the module dynamically
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and hasattr(obj, "execute"):  # has an execute() method
                    command_name = name.replace("Command", "").lower()  #(AdditionCommand → add)
                    self.register_command(command_name, obj())

    def register_command(self, command_name, command):
        """Registers a command in the command dictionary."""
        self.commands[command_name] = command

    def execute_command(self, command_input):
        """Executes a registered command or handles special commands like 'exit' and 'help'."""
        parts = command_input.strip().split()
        if not parts:
            return

        command_name, *args = parts
        command_name = command_name.lower()

        if command_name == 'exit':
            print("Goodbye!")
            sys.exit()
        elif command_name == 'help':
            print("Available commands:", ", ".join(self.commands.keys()))
            return

        command = self.commands.get(command_name)
        if command:
            try:
                command.execute(*args)
            except Exception as e: # pylint: disable=broad-exception-caught
                print(f"Error executing '{command_name}': {e}")
        else:
            print(f"Unknown command: {command_name}")
