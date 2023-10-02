def callLimit(limit: int) -> None:
    """
    A decorator function that limits execution of a function
    """

    def callLimiter(function) -> None:
        """
        A wrapper function that sets up the limiter for given function
        """

        # amount of times given function is called
        count = 0

        def limit_function(*args: any, **kwds: any) -> any:
            """
            A function that blocks execution of given function
            if called more times than the given limit
            """

            # declare non local variables
            nonlocal count

            # increment counter
            count += 1

            # make sure function isn't called more times than the limit
            if count > limit:
                return print(f"Error: {function} call too many times")

            # call the function
            return function(*args, *kwds)

        # return the function
        return limit_function

    # return the limiter
    return callLimiter
