import sys as Sys


# docstrings are used to document
# functions, methods, classes, scripts/programs, modules and packages
# there are various conventions for docstrings but they usually contain
#   functions/methods:
#       - short description of its behavior
#       - details of the accepted arguments
#       - details of the return value/s
#       - exceptions that could be raised
#       - short examples of its usage
#   classes:
#       - short description of the subject
#       - short descriptions of its methods
#       - short descriptions of its attributes
#   scripts/programs:
#       - short description of its behavior
#       - details of the accepted arguments
#       - details of the output
#       - short descriptions of its functions
#   modules:
#       - short description of the subject
#       - lists its exported
#           - classes
#           - functions
#           - variables
#           - exceptions
#   packages:
#       - short description of the subject
#       - lists its exported
#           - modules
#           - sub-packages
def main():
    """
    A program that counts different characters of a given string

    Arguments:
        a single string
        prompts for one if not given

    Outputs:
        formatted string that contains
        - length of the string
        - amount of uppercase characters
        - amount of lowercase characters
        - amount of punctuation marks
        - amount of space characters
        - amount of digits
    """

    # hide the traceback of assertion errors
    Sys.tracebacklimit = 0

    # punctuation characters
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # make sure there's no more than one argument
    assert len(Sys.argv) <= 2, "more than one argument is provided"

    # extract the string
    try:
        string = Sys.argv[1]
    except IndexError:
        string = input("What is the text to count?\n")

    # length of string
    length = len(string)

    # amount of uppercase letters
    upper_count = sum([char.isupper() for char in string])

    # amount of lowercase letters
    lower_count = sum([char.islower() for char in string])

    # amount of punctuation marks
    punctuation_count = sum([char in punctuation for char in string])

    # amount of space characters
    space_count = sum([char.isspace() for char in string])

    # amount of digits
    digit_count = sum([char.isdigit() for char in string])

    # print according to pdf
    print(f"The text contains {length} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
