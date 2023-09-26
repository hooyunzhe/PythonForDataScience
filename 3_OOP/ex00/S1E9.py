from abc import ABC, abstractmethod


class Character(ABC):
    """
    A class that represents a character

    Methods:
        (abstract) die() -> None: un-alives the character

    Attributes:
        first_name (str): first name of the character
        is_alive (bool): alive status of the character
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the abstract class with a first name and alive status

        Arguments:
            first_name (str): first name of the character
            is_alive (bool): alive status of the character (True by default)
        """

        # set the attributes
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """
        An abstract method can be declared by using
        the @abstractmethod decorator

        This method is supposed to un-alive the character
        """


class Stark(Character):
    """
    A subclass that inherits from Character and implements the method "die"

    Methods:
        (implemented) die() -> None: un-alives the character

    Attributes:
        (inherited) first_name (str): first name of the character
        (inherited) is_alive (bool): alive status of the character
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the subclass with the given values by
        passing them to the __init__ method of the parent class

        Arguments:
            first_name (str): first name of the character
            is_alive (bool): alive status of the character (True by default)
        """

        # pass arguments to the parent
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Implement the abstract method from the parent

        Un-alive the character
        """

        # set the attribute
        self.is_alive = False
