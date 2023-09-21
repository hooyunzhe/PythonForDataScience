import sys as Sys

# hide the traceback of assertion errors
Sys.tracebacklimit = 0

# make sure there's no more than one argument
assert len(Sys.argv) <= 2, "more than one argument is provided"

# if an argument is provided
if len(Sys.argv) == 2:
    # extract the argument
    arg = Sys.argv[1]

    # make sure it's an integer
    try:
        number = int(arg)
    except ValueError:
        # don't provide context to hide the extra message
        raise AssertionError("argument is not an integer") from None

    # check if it's even or odd
    even_odd = "Even" if number % 2 == 0 else "Odd"

    # print the result
    print(f"I'm {even_odd}")
