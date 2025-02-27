from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A King class inheriting from Baratheon and Lannister."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a King with default brown eyes and dark hair."""
        super().__init__(first_name, is_alive)
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, color):
        """Set the eye color of the King."""
        self.eyes = color

    def get_eyes(self):
        """Return the eye color of the King."""
        return self.eyes

    def set_hairs(self, color):
        """Set the hair color of the King."""
        self.hairs = color

    def get_hairs(self):
        """Return the hair color of the King."""
        return self.hairs
