import math


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    A function that calculates and prints the
    requested statistics of the given numbers

    Arguments:
        *args (any): numbers to calculate statistics with
        **kwargs (any): statistics to calculate with pairs of
            any one of below keywords:
                [toto, tutu, tata, hello, world]
            and any one of below values:
                [mean, median, quartile, std, var]
    """

    # accepted keywords
    keys = ["toto", "tutu", "tata", "hello", "world"]

    # accepted values
    values = ["mean", "median", "quartile", "std", "var"]

    for key, value in kwargs.items():
        if key in keys and value in values:
            if len(args) > 0:
                eval(value)(sorted(args))
            else:
                print("ERROR")


def mean(numbers: list[int]) -> None:
    """
    Calculate and print the mean of the numbers
    """

    # sum over the length
    print(f"mean : {sum(numbers) / len(numbers)}")


def median(numbers: list[int]) -> None:
    """
    Calculate and print the median of the numbers
    """

    # value at the middle (odd amount of numbers)
    # average of values above/below the middle (even amount of numbers)
    amount = len(numbers)
    midpoint = amount // 2
    if amount % 2 != 0:
        print(f"median : {numbers[midpoint]}")
    else:
        print(f"median : {(numbers[midpoint - 1] + numbers[midpoint]) / 2}")


def quartile(numbers: list[int]) -> None:
    """
    Calculate and print the lower and upper quartiles of the numbers
    """

    # first divide the numbers into 4 parts
    # lower quartile is the value between the first and second parts
    # upper quartile is the value between the third and forth parts
    amount = len(numbers)
    print(f"quartile : [{numbers[amount // 4]}, {numbers[amount // 4 * 3]}]")


def std(numbers: list[int]) -> None:
    """
    Calculate and print the standard deviation of the numbers
    """

    # standard deviation is the square root of the variance,
    # which is the sum of squared differences between
    # each number and the average over the amount of numbers
    average = sum(numbers) / len(numbers)
    squared_difference_sum = sum((n - average) ** 2 for n in numbers)
    print(f"std : {math.sqrt(squared_difference_sum / len(numbers))}")


def var(numbers: list[int]) -> None:
    """
    Calculate and print the variance of the numbers
    """

    # variance is the sum of squared differences between
    # each number and the average over the amount of numbers
    average = sum(numbers) / len(numbers)
    print(f"var : {sum((n - average) ** 2 for n in numbers) / len(numbers)}")
