from S1E7 import Baratheon, Lannister


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
Robert = Baratheon("Robert")

# should set first name and House attributes correctly
assert_equals(
    "Robert.__dict__",
    Robert.__dict__,
    {'first_name': 'Robert', 'is_alive': True,
     'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
)

# should override built-ins to return House attribtues
assert_equals(
    "str(Robert.__str__)",
    str(Robert.__str__),
    ("<bound method Baratheon.__str__ of "
     "Vector: ('Baratheon', 'brown', 'dark')>")
)
assert_equals(
    "str(Robert.__repr__)",
    str(Robert.__repr__),
    ("<bound method Baratheon.__repr__ of "
     "Vector: ('Baratheon', 'brown', 'dark')>")
)

# should un-alive the character
assert_equals("Robert.is_alive", Robert.is_alive, True)
Robert.die()
assert_equals("Robert.is_alive", Robert.is_alive, False)

# should have docstring
assert_equals("type(Robert.__doc__)", type(Robert.__doc__), str)

print("----------------------------------------------------------------------")

# instantiate the subclass
Cersei = Lannister("Cersei")

# should set first name and House attributes correctly
assert_equals(
    "Cersei.__dict__",
    Cersei.__dict__,
    {'first_name': 'Cersei', 'is_alive': True,
     'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'})

# should override built-ins to return House attributes
assert_equals(
    "str(Cersei.__str__)",
    str(Cersei.__str__),
    ("<bound method Lannister.__str__ of "
     "Vector: ('Lannister', 'blue', 'light')>")
)
assert_equals(
    "str(Cersei.__repr__)",
    str(Cersei.__repr__),
    ("<bound method Lannister.__repr__ of "
     "Vector: ('Lannister', 'blue', 'light')>")
)

# should un-alive the character
assert_equals("Cersei.is_alive", Cersei.is_alive, True)
Cersei.die()
assert_equals("Cersei.is_alive", Cersei.is_alive, False)

# should have docstring
assert_equals("type(Cersei.__doc__)", type(Cersei.__doc__), str)

print("----------------------------------------------------------------------")

# instantiate using the static method
Jaine = Lannister.create_lannister("Jaine", True)

# should be the same as the normal constructor
assert_equals("type(Jaine).__name__", type(Jaine).__name__, "Lannister")
assert_equals(
    "Jaine.__dict__",
    Jaine.__dict__,
    {'first_name': 'Jaine', 'is_alive': True,
     'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'})
assert_equals(
    "str(Jaine.__str__)",
    str(Jaine.__str__),
    ("<bound method Lannister.__str__ of "
     "Vector: ('Lannister', 'blue', 'light')>")
)
assert_equals(
    "str(Jaine.__repr__)",
    str(Jaine.__repr__),
    ("<bound method Lannister.__repr__ of "
     "Vector: ('Lannister', 'blue', 'light')>")
)
assert_equals("Jaine.is_alive", Jaine.is_alive, True)
Jaine.die()
assert_equals("Jaine.is_alive", Jaine.is_alive, False)
assert_equals("type(Jaine.__doc__)", type(Jaine.__doc__), str)
