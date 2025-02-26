from app.command import Command

class DivideCommand(Command):
    def execute(self, *args):
        """Perform division, handling division by zero and missing arguments."""
        if not args: 
            return "Error: Missing arguments"
        
        try:
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    return "Error: Division by zero"
                result /= num
            return result
        except ZeroDivisionError: # pragma: no cover
            return "Error: Division by zero" # pragma: no cover
