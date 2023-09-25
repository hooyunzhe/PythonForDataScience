from load_image import ft_load


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
assert_raises(ft_load, 42)

# path must be valid
assert_raises(ft_load, "42.jpg", expected_exception=FileNotFoundError)

# should print shape (257, 450, 3)
# should return 3D array of pixels in RGB
# first 3 pixels should be
# [[[19 42 83]
#   [23 42 84]
#   [28 43 84]
# last 3 pixels should be
#   [ 0 0 0]
#   [ 1 1 1]
#   [ 1 1 1]]]
# numpy arrays allow multi dimensional slicing
# array = ft_load("landscape.jpg")
# print(array[0, 0:3])
# print(array[-1, -3:])
print(ft_load("landscape.jpg"))
