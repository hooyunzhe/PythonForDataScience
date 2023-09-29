class calculator:
    """
    A class that represents a simple calculator
    for calculations between two vectors

    Methods:
        dotproduct(V1: list[float], V2: list[float]) -> None:
            calculate the dot product of the vectors
        add_vec(V1: list[float], V2: list[float]) -> None:
            add the vectors together
        sous_vec(V1: list[float], V2: list[float]) -> None:
            subtract the second vector from the first
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of the vectors and print it

        Arguments:
            V1 (list[float]): the first vector
            V2 (list[float]): the second vector
        """

        # calculate and print the dot product
        print(sum(n1 * n2 for n1, n2 in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add the vectors together and print the result

        Arguments:
            V1 (list[float]): the first vector
            V2 (list[float]): the second vector
        """

        # calculate and print the result
        print([n1 + n2 for n1, n2 in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first and print the result

        Arguments:
            V1 (list[float]): the first vector
            V2 (list[float]): the second vector
        """

        # calculate and print the result
        print([n1 - n2 for n1, n2 in zip(V1, V2)])
