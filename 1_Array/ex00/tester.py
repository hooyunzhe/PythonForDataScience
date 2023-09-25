from give_bmi import give_bmi, apply_limit


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


def assert_equals(function_to_test, *args, expected_output):
    arg_list = str(list(args))[1:-1]
    print(f"\033[0;36m{function_to_test.__name__}({arg_list}):\033[0m", end="")
    try:
        output = function_to_test(*args)
        assert output == expected_output
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;32m\033[3mReturns {output}\033[0m")
    except AssertionError as e:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{type(e).__name__}: {e}\033[0m")


# arguments must be lists
assert_raises(give_bmi, 42, [42])
assert_raises(give_bmi, [42], "42")

# lists must be the same size
assert_raises(give_bmi, [1], [1, 2])

# lists must only contain ints or floats
assert_raises(give_bmi, ["42"], [42])
assert_raises(give_bmi, [42], ["42"])

# values must be within range
assert_raises(give_bmi, [0], [80])
assert_raises(give_bmi, [1.8], [0])
assert_raises(give_bmi, [180], [80])
assert_raises(give_bmi, [1.8], [80000])

# check calculated BMIs
# should return below values
# 165.3 squared / 2.71 = 22.507863455018317
# 38.4 squared / 1.15 = 29.0359168241966
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmis = [22.507863455018317, 29.0359168241966]
bmi = give_bmi(height, weight)
assert_equals(give_bmi, height, weight, expected_output=bmis)

# arguments must be a list and an int
assert_raises(apply_limit, 42, 42)
assert_raises(apply_limit, [42], "42")

# list must only contain ints or floats
assert_raises(apply_limit, ["42"], 42)

# should return below values
# 22.507863455018317 > 26 = False
# 29.0359168241966 > 26 = True
bools = [False, True]
assert_equals(apply_limit, bmi, 26, expected_output=bools)
