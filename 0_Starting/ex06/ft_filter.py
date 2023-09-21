def ft_filter(function, iterable):
    """
    A function that filters an iterable based on the given function

    Arguments:
        a function or None
        an iterable

    Returns:
        the filtered iterable
    """

    # if a function is provided:
    #   list of elements for which function(element) returns true
    # if no function is provided:
    #   list of elements that are true
    return [element for element in iterable
            if (function(element) if function else element)]
