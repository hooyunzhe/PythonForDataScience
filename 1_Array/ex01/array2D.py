import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    A function that truncates a 2D array and
    print its shape before and after

    Arguments:
        family (list): 2D array to be truncated
        start (int): index to truncate from
        end (int): index to truncate until

    Returns:
        the truncated list
    """

    # make sure family is a list of lists
    assert type(family) is list, "family must be a list"
    assert all(type(lst) is list for lst in family), (
        "family must only contain lists")

    # make sure start and end are ints
    assert type(start) is int, "start must be an int"
    assert type(end) is int, "end must be an int"

    # make sure family only contains lists of the same size
    length_to_check = len(family[0])
    same_size = all(len(lst) == length_to_check for lst in family)
    assert same_size, "family must only contain lists of the same size"

    # convert family to a numpy array
    family_array = np.array(family)

    # print the original shape
    print(f"My shape is : {family_array.shape}")

    # truncate the array
    truncated_array = family_array[start:end]

    # print the shape after truncation
    print(f"My new shape is : {truncated_array.shape}")

    # return the truncated array
    return truncated_array.tolist()
