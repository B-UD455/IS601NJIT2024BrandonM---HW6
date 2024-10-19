Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from abc import ABC, abstractmethod
... 
... class Command(ABC):
...     @abstractmethod
...     def execute(self):
...         pass
... 
... class CommandHandler:
...     def __init__(self):
...         self.commands = {}
... 
...     def register_command(self, command_name: str, command: Command):
...         self.commands[command_name] = command
... 
...     def execute_command(self, command_name: str):
...         """ Look before you leap (LBYL) - Use when its less likely to work
...         if command_name in self.commands:
...             self.commands[command_name].execute()
...         else:
...             print(f"No such command: {command_name}")
...         """
...         """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
...         try:
...             self.commands[command_name].execute()
...         except KeyError:
