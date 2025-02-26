from app.command import Command  # Fix circular import

class SubtractCommand(Command):
    def execute(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
