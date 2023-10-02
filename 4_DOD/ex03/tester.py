from new_student import Student


def assert_raises(
    function_to_test,
    expected_exception=AssertionError,
    *args, **kwargs
):
    arg_list = str(list(args))[1:-1]
    print(f"\033[0;36m{function_to_test.__name__}({arg_list}):\033[0m", end="")
    try:
        function_to_test(*args, **kwargs)
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


# the @dataclass decorator turns classes into dataclasses,
# which are similar to "structs" in C
# the special methods are automatically generated based on the attributes
# attributes can have defaults and can be non-initializable

# instantiate the dataclass
student = Student(name="Edward", surname="agle")

# should set attributes correctly
assert_equals("student.name", student.name, "Edward")
assert_equals("student.surname", student.surname, "agle")
assert_equals("student.active", student.active, True)
assert_equals("student.login", student.login, "Eagle")

# should print
# Student(
#   name='Edward', surname='agle',
#   active=True, login='Eagle',
#   id='randomly_generated_id')
print(student)

# should not be able to instantiate with non-initializable attributes
assert_raises(
    Student,
    name="Edward", surname="agle", id="toto",
    expected_exception=TypeError
)
assert_raises(
    Student,
    name="Edward", surname="agle", login="Eagle",
    expected_exception=TypeError
)
