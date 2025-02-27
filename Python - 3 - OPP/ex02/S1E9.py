from abc import ABC, abstractmethod


class Character(ABC):
    """This is the Abstract Charater Class"""

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def is_alive(self):
        """Return the charachters life status"""
        return (self.is_alive)

    @abstractmethod
    def die(self):
        """Abstract method"""
        self.is_alive = False


class Stark(Character):
    """Stark class inherited from the Character Class"""

    def die(self):
        """This function changes the is_alive atribut to false"""
        self.is_alive = False
