from app.command import Command  # Fix circular import

class MultiplyCommand(Command):
    def execute(self, *args):
        result = 1
        for num in args:
            result *= num
        return result
