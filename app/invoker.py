class CommandInvoker:
    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        self.commands[name] = command

    def execute(self, name, *args):
        """Execute a registered command, return error if command doesn't exist."""
        if name in self.commands:
            return self.commands[name].execute(*args)
        return "Invalid command"
