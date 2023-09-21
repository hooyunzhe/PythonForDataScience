import sys as Sys
from ft_filter import ft_filter


def main():
    """
    A program that counts the amount of words
    that are longer than N characters

    Arguments:
        a single string
        an integer

    Outputs:
        list of words that are longer than N characters
    """

    # hide the traceback of assertion errors
    Sys.tracebacklimit = 0

    # make sure there's no more than one argument
    assert len(Sys.argv) == 3, "the arguments are bad"

    # make sure the second argument is an integer
    try:
        number = int(Sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad") from None

    # extract the string
    string = Sys.argv[1]

    # extract the words from the string
    words = [word for word in string.split() if word.isalpha()]

    # print the filtered words
    print(ft_filter(lambda word: len(word) > number, words))


if __name__ == "__main__":
    main()
