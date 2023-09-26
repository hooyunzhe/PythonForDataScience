from S1E9 import Character, Stark


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


def assert_equals(name, value, expected_value):
    print(f"\033[0;36m{name}:\033[0m", end="")
    try:
        assert value == expected_value
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;32m\033[3m{name} equals {expected_value}\033[0m")
    except AssertionError:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{name} does not equal {expected_value}\033[0m")


# instantiate the subclass
Ned = Stark("Ned")

# should set first name correctly
# should have default value for is_alive
assert_equals(
    "Ned.__dict__",
    Ned.__dict__,
    {'first_name': 'Ned', 'is_alive': True}
)
assert_equals("Ned.is_alive", Ned.is_alive, True)

# should un-alive the character
Ned.die()
assert_equals("Ned.is_alive", Ned.is_alive, False)

# should have docstrings
assert_equals("type(Ned.__doc__)", type(Ned.__doc__), str)
assert_equals("type(Ned.__init__.__doc__)", type(Ned.__init__.__doc__), str)
assert_equals("type(Ned.die.__doc__)", type(Ned.die.__doc__), str)

# instantiate with alive status
Lyanna = Stark("Lyanna", False)

# should set first name and alive status correctly
assert_equals(
    "Lyanna.__dict__",
    Lyanna.__dict__,
    {'first_name': 'Lyanna', 'is_alive': False}
)

# should not be able to instantiate abstract class
assert_raises(Character, "hodor", expected_exception=TypeError)
