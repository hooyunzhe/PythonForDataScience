from array2D import slice_me


def assert_raises(function_to_test, *args, expected_exception=AssertionError):
    print(f"\033[0;36m{function_to_test.__name__}{args}:\033[0m ", end="")
    try:
        function_to_test(*args)
        print("\033[0;31mTest failed\033[0m")
        print("	\033[3;31m\033[3mNo exceptions were raised\033[0m")
    except expected_exception as e:
        print("\033[0;32mTest passed\033[0m")
        print(f"	\033[2;35m\033[3mRaises [{type(e).__name__}: {e}]\033[0m")
    except Exception as e:
        print("\033[0;31mTest failed\033[0m")
        print(f"	\033[3;31m{type(e).__name__}: {e}\033[0m")


# initialize the 2D array
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

# first argument must be a list of lists with the same size
assert_raises(slice_me, 42, 0, 1)
assert_raises(slice_me, [42], 0, 1)
assert_raises(slice_me, [[42], [1, 2]], 0, 1)

# second / third argument must be ints
assert_raises(slice_me, [[42]], "0", 1)
assert_raises(slice_me, [[42]], 0, "1")

# should print shapes (4, 2) and (2, 2)
# should return [[1.8, 78.4], [2.15, 102.7]]
print(slice_me(family, 0, 2))

# should print shapes (4, 2) and (1, 2)
# should return [[2.15, 102.7]]
print(slice_me(family, 1, -2))
