def count_in_list(to_count: list, target: str) -> int:
    """
    A function that counts occurrences of the given string

    Arguments:
        to_count (list): the list of strings to search from
        target (str): the string to count occurrences with

    Returns:
        the number of occurrences
    """

    # the amount of times the target string appears in the list
    return len([string for string in to_count if string == target])
