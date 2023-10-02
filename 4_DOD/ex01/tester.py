from in_out import outer, square, pow


def assert_equals(name, value, expected_value):
    print(f"\033[0;36m{name}:\033[0m", end="")
    try:
        assert value == expected_value
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;32m\033[3m{name} equals {expected_value}\033[0m")
    except AssertionError:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{name} does not equal {expected_value}\033[0m")


# initialize the function
my_counter = outer(3, square)

# should return 9 (3*3)
assert_equals("my_counter()", my_counter(), 9)

# should return 81 (9*9)
assert_equals("my_counter()", my_counter(), 81)

# should return 6561 (81*81)
assert_equals("my_counter()", my_counter(), 6561)

# initialize the function
another_counter = outer(1.5, pow)

# should return 1.8371173070873836 (1.5^1.5)
assert_equals("another_counter()", another_counter(), 1.8371173070873836)

# should return 3.056683336818703 (1.8371173070873836^1.8371173070873836)
assert_equals("another_counter()", another_counter(), 3.056683336818703)

# should return 30.42684786675409 (3.056683336818703^3.056683336818703)
assert_equals("another_counter()", another_counter(), 30.42684786675409)
