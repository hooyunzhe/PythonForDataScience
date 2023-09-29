from ft_calculator import calculator


def assert_equals(name, value, expected_value):
    print(f"\033[0;36m{name}:\033[0m", end="")
    try:
        assert value == expected_value
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;32m\033[3m{name} equals {expected_value}\033[0m")
    except AssertionError:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{name} does not equal {expected_value}\033[0m")


# Python operators for classes can be overloaded by
# overriding special methods such as
#   __add__ for +
#   __mul__ for *
#   __sub__ for -
#   __truediv__ for /

# instantiate the class
v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])

# should apply addition to all numbers in the list
v1 + 5
assert_equals("v1.vector", v1.vector, [5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

# instantiate the class
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])

# should apply multiplication to all numbers in the list
v2 * 5
assert_equals("v2.vector", v2.vector, [0.0, 5.0, 10.0, 15.0, 20.0, 25.0])

# instantiate the class
v3 = calculator([10.0, 15.0, 20.0])

# should apply subtraction and division to all numbers in the list
v3 - 5
assert_equals("v3.vector", v3.vector, [5.0, 10.0, 15.0])
v3 / 5
assert_equals("v3.vector", v3.vector, [1.0, 2.0, 3.0])
