from load_csv import load


def assert_raises(function_to_test, *args, expected_exception=AssertionError):
    arg_list = str(list(args))[1:-1]
    print(f"\033[0;36m{function_to_test.__name__}({arg_list}):\033[0m", end="")
    try:
        function_to_test(*args)
        print("\033[0;31m Test failed\033[0m")
        print("	\033[3;31m\033[3mNo exceptions were raised\033[0m")
    except expected_exception as e:
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;35m\033[3mRaises [{type(e).__name__}: {e}]\033[0m")
    except Exception as e:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{type(e).__name__}: {e}\033[0m")


# path must be a string
assert_raises(load, 42)

# path must be valid
assert_raises(load, "42.csv")

# should print shape (195, 302)
# should return DataFrame of life expectancy of countries
# column headers should be
#   country 1800 1801 ... 2100
# first row should be
#   Afghanistan 28.2 28.2 ... 76.8
#
# pandas DataFrames have multiple ways of indexing
#   by label/position using [column] (row position for slicing)
#   by label using .loc[row, column]
#   by position using .iloc[row, column]
# all of the above support multiple types of input
#   single label/index
#   list/array of labels/indices
#   slice object of label/index (the stop label is included)
#   boolean array
#   callable that takes in a DataFrame and returns one of the above
#
# df = load("life_expectancy_years.csv")
# print(df.loc[0:5, ["country", "1800","1801", "2100"]])
print(load("life_expectancy_years.csv"))
