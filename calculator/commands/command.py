""" Calculator Command Module

Commands:
    - AdditionCommand: Handles addition operations
    - SubtractionCommand: Handles subtraction operations
    - MultiplicationCommand: Handles multiplication operations
    - DivisionCommand: Handles division operations
    - MenuCommand: Displays available calculator operations

"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for all commands."""

    @abstractmethod
    def execute(self):
        """Abstract method to be implemented by concrete commands"""


def start():
    """Start the calculator REPL"""
    # pylint: disable=import-outside-toplevel
    from calculator.commands import (
        CommandHandler, AdditionCommand, SubtractionCommand,
        MultiplicationCommand, DivisionCommand, MenuCommand
    )

    command_handler = CommandHandler()

    # Register commands
    command_handler.register_command("add", AdditionCommand())
    command_handler.register_command("subtract", SubtractionCommand())
    command_handler.register_command("multiply", MultiplicationCommand())
    command_handler.register_command("divide", DivisionCommand())
    command_handler.register_command("menu", MenuCommand())

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
            print(f"Input error: {e}")
        except TypeError as e:
            print(f"Type error: {e}")
        except AttributeError as e:
            print(f"Command error: {e}")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Unexpected error: {e}")
