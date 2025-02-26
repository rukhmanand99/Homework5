class Command:
    def execute(self, *args):
        """Base command class, must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement execute()")
