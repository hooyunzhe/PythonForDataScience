import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    A function that calculates BMIs from given heights and weights

    Arguments:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        a list of BMIs calculated from the input
    """

    # make sure the arguments are lists
    assert type(height) is list, "height must be a list"
    assert type(weight) is list, "weight must be a list"

    # convert to numpy arrays
    height_array = np.array(height)
    weight_array = np.array(weight)

    # make sure the two lists are the same size
    assert height_array.size == weight_array.size, (
        "height and weight must have the same size")

    # make sure the lists only contain ints or floats
    #
    # by default, numpy.array converts python int/float types to
    # numpy.int64/float64 types which are sub types of numpy.number

    assert np.issubdtype(height_array.dtype, np.number), (
        "height must only contain ints or floats")
    assert np.issubdtype(weight_array.dtype, np.number), (
        "weight must only contain ints or floats")

    # make sure the values are within the expected range
    #
    # numpy arrays support broadcasting when using operators
    # which means they will be applied to each element
    #
    # for boolean arrays, logical operators can be used
    # instead of their functional equivalents
    assert np.all(np.logical_and(height_array > 0, height_array <= 3)), (
        "heights must be in meters and not zero")
    assert np.all(np.logical_and(weight_array > 0, weight_array <= 1000)), (
        "weights must be in kilograms and not zero")

    # the calculated BMIs
    return np.divide(weight_array, np.power(height_array, 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    A function that transforms given list of BMIs to
    booleans indicating whether each is above the limit

    Arguments:
        bmi (list[int | float]): list of BMIs to transform
        limit (int): BMIs have to be above this limit

    Returns:
        a list of booleans where True means above the limit
    """

    # make sure the arguments are a list and an int
    assert type(bmi) is list, "bmi must be a list"
    assert type(limit) is int, "limit must be an int"

    # convert to numpy array
    bmi_array = np.array(bmi)

    # make sure the list only contains ints or floats
    assert np.issubdtype(bmi_array.dtype, np.number), (
        "bmi must only contain ints or floats")

    # transform the list
    return np.greater(bmi_array, limit).tolist()
