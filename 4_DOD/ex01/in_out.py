def square(x: int | float) -> int | float:
    """
    A function that returns the square of given number
    """

    # calculate and return the square
    return x * x


def pow(x: int | float) -> int | float:
    """
    A function that returns the exponentiation of given number with itself
    """

    # calculate and return the exponentiation
    return x ** x


def outer(x: int | float, function) -> object:
    """
    A wrapper function that returns an object which when called,
    returns the result from calling the given function with the given number

    Arguments:
        x (int | float): number to do calculations with
        function: callable that does calculations with given number

    Returns:
        object: when called, returns the result of calculations
    """

    # amount of times the object is called
    count = 0
    result = x

    def inner() -> float:
        """
        A function that does calculations with given number and function
        """

        # nonlocal keyword declares that the variable is not local and instead
        # references the nearest enclosing scope (usually the parent function)
        nonlocal count
        nonlocal result

        # increment count
        count += 1

        # calculate and return the new result
        result = function(result)
        return result

    # return the function
    return inner
