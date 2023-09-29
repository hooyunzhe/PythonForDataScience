class calculator:
    """
    A class that represents a simple calculator
    for calculations between a vector and a scalar

    Methods:
        __add__(scalar: int | float) -> None: [overridden]
            apply addition to the vector
        __mul__(scalar: int | float) -> None: [overridden]
            apply multiplication to the vector
        __sub__(scalar: int | float) -> None: [overridden]
            apply subtraction to the vector
        __truediv__(scalar: int | float) -> None: [overridden]
            apply division to the vector

    Attribute:
        vector (list[float]): vector of numbers
    """

    def __init__(self, vector: list[float]):
        """
        Initialize with the given vector

        Argument:
            vector (list[float]): list of numbers to do calculations on
        """

        # set the attribute
        self.vector = vector

    def __add__(self, scalar: int | float) -> None:
        """
        Override the built-in to apply addition of the scalar
        to the numbers in the vector and print the vector

        Argument:
            scalar (int | float): scalar to add
        """

        # apply addition to the vector
        self.vector = [n + scalar for n in self.vector]

        # print the vector post addition
        print(self.vector)

    def __mul__(self, scalar: int | float) -> None:
        """
        Override the built-in to apply multiplication of the scalar
        to the numbers in the vector and print the vector

        Argument:
            scalar (int | float): scalar to multiply
        """

        # apply multiplication to the vector
        self.vector = [n * scalar for n in self.vector]

        # print the vector post multiplication
        print(self.vector)

    def __sub__(self, scalar: int | float) -> None:
        """
        Override the built-in to apply subtraction of the scalar
        to the numbers in the vector and print the vector

        Argument:
            scalar (int | float): scalar to subtract
        """

        # apply subtraction to the vector
        self.vector = [n - scalar for n in self.vector]

        # print the vector post subtraction
        print(self.vector)

    def __truediv__(self, scalar: int | float) -> None:
        """
        Override the built-in to apply division of the scalar
        to the numbers in the vector and print the vector

        Argument:
            scalar (int | float): scalar to divide
        """

        # make sure scalar is not 0 to prevent division by 0
        assert scalar != 0, "cannot divide by zero"

        # apply division to the vector
        self.vector = [n / scalar for n in self.vector]

        # print the vector post division
        print(self.vector)
