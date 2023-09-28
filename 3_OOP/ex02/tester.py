from DiamondTrap import King


def assert_equals(name, value, expected_value):
    print(f"\033[0;36m{name}:\033[0m", end="")
    try:
        assert value == expected_value
        print("\033[0;32m Test passed\033[0m")
        print(f"	\033[2;32m\033[3m{name} equals {expected_value}\033[0m")
    except AssertionError:
        print("\033[0;31m Test failed\033[0m")
        print(f"	\033[3;31m{name} does not equal {expected_value}\033[0m")


# Since Python 2.3, the language uses the C3 linearization algorithm
# as the default algorithm for Method Resolution, which handles
# cases such as diamond inheritance

# instantiate the class
Joffrey = King("Joffrey")

# should have setters and getters
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
assert_equals("Joffrey.get_eyes()", Joffrey.get_eyes(), "blue")
assert_equals("Joffrey.get_hairs()", Joffrey.get_hairs(), "light")
assert_equals(
    "Joffrey.__dict__",
    Joffrey.__dict__,
    {'first_name': 'Joffrey', 'is_alive': True,
     'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
)

# should match the Baratheon class constructor
assert_equals(
    "str(Joffrey.__str__)",
    str(Joffrey.__str__),
    ("<bound method Baratheon.__str__ of "
     "Vector: ('Baratheon', 'blue', 'light')>")
)
assert_equals(
    "str(Joffrey.__repr__)",
    str(Joffrey.__repr__),
    ("<bound method Baratheon.__repr__ of "
     "Vector: ('Baratheon', 'blue', 'light')>")
)
assert_equals("Joffrey.is_alive", Joffrey.is_alive, True)
Joffrey.die()
assert_equals("Joffrey.is_alive", Joffrey.is_alive, False)
assert_equals("type(Joffrey.__doc__)", type(Joffrey.__doc__), str)
