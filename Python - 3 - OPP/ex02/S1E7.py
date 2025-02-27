from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Init method"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Barathon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Returns a user-friendly string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a developer-friendly representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """This function changes the is_alive atribut to false"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Init method"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "leicht"

    def __str__(self):
        """Returns a user-friendly string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a user-friendly string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Method with @classmethod decorator"""
        return cls(name)

    def die(self):
        """This function changes the is_alive atribut to false"""
        self.is_alive = False
