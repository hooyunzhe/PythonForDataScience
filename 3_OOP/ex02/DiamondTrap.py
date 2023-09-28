from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class that represents a King
    [parent classes: Baratheon, Lannister]

    Methods:
        die() -> None: [inherited]
            un-alives the character
        __str__() -> str: [inherited]
            returns the string representation
        __repr__() -> str: [inherited]
            returns the string representation
        get_eyes() -> str:
            returns the color of the character's eyes
        get_hairs() -> str:
            returns the shade of the character's hair
        set_eyes(color: str) -> None:
            changes the color of the character's eyes
        set_hairs(shade: str) -> None:
            changes the shade of the character's hair

    Attributes:
        first_name (str): [inherited]
            first name of the character
        is_alive (bool): [inherited]
            alive status of the character
        family_name (str): [inherited]
            family name of the character
        eyes (str): [inherited]
            color of the character's eyes
        hairs (str): [inherited]
            shade of the character's hair
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the class with the given values and the
        appropriate attributes of the House of Baratheon

        Arguments:
            first_name (str):
                first name of the character
            is_alive (bool): [default True]
                alive status of the character
        """

        # pass arguments to the parent
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """
        Return the color of the character's eyes
        """

        # return the attribute
        return self.eyes

    def get_hairs(self) -> str:
        """
        Return the shade of the character's hairs
        """

        # return the attribute
        return self.hairs

    def set_eyes(self, color: str) -> None:
        """
        Change the color of the character's eyes
        """

        # set the attribute
        self.eyes = color

    def set_hairs(self, shade: str) -> None:
        """
        Change the shade of the character's hairs
        """

        # set the attribute
        self.hairs = shade
