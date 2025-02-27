class calculator:
    """Simple calculator"""

    def __init__(self, values):
        """Initialize with a list of numbers."""
        self.values = values

    def __add__(self, object) -> None:
        """Add a number to each element."""
        new_values = [object + x for x in self.values]
        print(new_values)
        self.values = new_values

    def __mul__(self, object) -> None:
        """Multiply each element by a number."""
        new_values = [object * x for x in self.values]
        print(new_values)
        self.values = new_values

    def __sub__(self, object) -> None:
        """Subtract a number from each element."""
        new_values = [x - object for x in self.values]
        print(new_values)
        self.values = new_values

    def __truediv__(self, object) -> None:
        """Divide each element by a number (handles division by zero)."""
        try:
            new_values = [x / object for x in self.values]
            print(new_values)
            self.values = new_values
        except ZeroDivisionError as e:
            print(f"Error: {e}")
