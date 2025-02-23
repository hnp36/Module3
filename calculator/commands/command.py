class Command:
    """Base class for all commands."""
    
    def execute(self):
        raise NotImplementedError("Subclasses should implement this method.")
