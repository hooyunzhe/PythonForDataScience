from S1E9 import Character


class Baratheon(Character):
    """
    A class that represents the House of Baratheon
    [parent class: Character]

    Methods:
        die() -> None: [implemented]
            un-alives the character
        __str__() -> str: [overridden]
            returns the string representation
        __repr__() -> str: [overridden]
            returns the string representation

    Attributes:
        first_name (str): [inherited]
            first name of the character
        is_alive (bool): [inherited]
            alive status of the character
        family_name (str):
            family name of the character
        eyes (str):
            color of the character's eyes
        hairs (str):
            shade of the character's hair
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the class with the given values and the
        appropriate attributes of the House of Baratheon

        Arguments:
            first_name (str):
                first name of the character
            is_alive (bool): [default: True]
                alive status of the character
        """

        # pass arguments to the parent
        super().__init__(first_name, is_alive)

        # set the attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
        Override the built-in to return the string representation
        of the House attributes instead of the object itself
        """

        # return the attributes of the House
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Override the built-in to return the string representation
        of the House attributes instead of the object itself
        """

        # return the attributes of the House
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """
        Implement the abstract method from the parent

        Un-alive the character
        """

        # set the attribute
        self.is_alive = False


class Lannister(Character):
    """
    A class that represents the House of Lannister
    [parent class: Character]

    Methods:
        die() -> None: [implemented]
            un-alives the character
        __str__() -> str: [overridden]
            returns the string representation
        __repr__() -> str: [overridden]
            returns the string representation
        create_lannister(first_name: str, is_alive: bool = True) -> Lannister:
            instantiates a new Lannister object

    Attributes:
        first_name (str): [inherited]
            first name of the character
        is_alive (bool): [inherited]
            alive status of the character
        family_name (str):
            family name of the character
        eyes (str):
            color of the character's eyes
        hairs (str):
            shade of the character's hair
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the class with the given values and the
        appropriate attributes of the House of Lannister

        Arguments:
            first_name (str):
                first name of the character
            is_alive (bool): [default: True]
                alive status of the character
        """

        # pass arguments to the parent
        super().__init__(first_name, is_alive)

        # set the attributes
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
        Override the built-in to return the string representation
        of the House attributes instead of the object itself
        """

        # return the attributes of the House
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Override the built-in to return the string representation
        of the House attributes instead of the object itself
        """

        # return the attributes of the House
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """
        Implement the abstract method from the parent

        Un-alive the character
        """

        # set the attribute
        self.is_alive = False

    @staticmethod
    def create_lannister(
        first_name: str,
        is_alive: bool = True
    ) -> "Lannister":
        """
        Static methods are bound to the class instead of the class objects,
        they can be called without a class object but cannot modify the state

        Instantiate a new Lannister object and return it

        Arguments:
            first_name (str):
                first name of the character
            is_alive (bool): [default: True]
                alive status of the character
        """

        # pass arguments to the constructor and return
        return Lannister(first_name, is_alive)
