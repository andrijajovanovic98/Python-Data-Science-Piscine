import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string as an ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass representing a student.
    """
    name: str
    surname: str
    active: bool = field(default=True)

    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Generates login and ID after initialization."""
        self.login = (self.name[0].upper() + self.surname.lower())
        self.id = generate_id()
