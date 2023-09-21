import sys as Sys


def main():
    """
    A program that encodes a string to Morse Code

    Arguments:
        a single string

    Outputs:
        Morse Code representing the given string
    """

    # list of Morse Codes of alphanumeric characters and space
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    # hide the traceback of assertion errors
    Sys.tracebacklimit = 0

    # make sure there's no more than one argument
    assert len(Sys.argv) == 2, "the arguments are bad"

    # make sure the string only contains alphanumeric characters
    assert Sys.argv[1].isalnum(), "the arguments are bad"

    # print the Morse Code representation of the string
    print("".join([NESTED_MORSE[char.upper()] for char in Sys.argv[1]])[:-1])


if __name__ == "__main__":
    main()
