from app.command import Command  # Fix circular import

class AddCommand(Command):
    def execute(self, *args):
        return sum(args)
