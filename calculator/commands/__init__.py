"""
This module defines the CommandHandler class, 
which manages and executes various calculator commands. 
It also includes a start function to launch a command-line interface (REPL) for user interaction.
"""
import sys
from .addition import AdditionCommand
from .substraction import SubtractionCommand
from .multiplication import MultiplicationCommand
from .division import DivisionCommand
from .menu_command import MenuCommand

class CommandHandler:
    """CommandHandler class manages the registration and execution of commands."""

    def __init__(self):
        """Initializes an empty command registry."""
        self.commands = {}

    def register_command(self, command_name, command):
        """Registers a command in the command dictionary."""
        self.commands[command_name] = command

    def execute_command(self, command_input):
        """Executes a registered command or handles special commands like 'exit' and 'help'."""
        if command_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
        elif command_input.lower() == 'help':
            print("Available commands:", ", ".join(self.commands.keys()))
            return

        command = self.commands.get(command_input.lower())
        if command:
            command.execute()
        else:
            print(f"Unknown command: {command_input}")

    def initialize_default_commands(self):
        """Initialize the default calculator commands."""
        self.register_command("add", AdditionCommand())
        self.register_command("subtract", SubtractionCommand())
        self.register_command("multiply", MultiplicationCommand())
        self.register_command("divide", DivisionCommand())
        self.register_command("menu", MenuCommand())

def start():
    """Start the calculator REPL"""
    command_handler = CommandHandler()
    command_handler.initialize_default_commands()

    print("\nWelcome to Calculator!")
    print("Type 'help' for available commands or 'exit' to quit.")
    MenuCommand().execute()

    while True:
        try:
            command = input("calculator> ").strip()
            command_handler.execute_command(command)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyError as e:
            print(f"Command not found: {e}")
        except RuntimeError as e:
            print(f"Runtime error: {e}")
        except (ImportError, AttributeError) as e:
            print(f"Module or command error: {e}")
