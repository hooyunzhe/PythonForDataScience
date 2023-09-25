from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np


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


# argument must be a 3D numpy array
assert_raises(ft_invert, 42)
assert_raises(ft_invert, np.array([42]))
assert_raises(ft_red, 42)
assert_raises(ft_red, np.array([42]))
assert_raises(ft_green, 42)
assert_raises(ft_green, np.array([42]))
assert_raises(ft_blue, 42)
assert_raises(ft_blue, np.array([42]))
assert_raises(ft_grey, 42)
assert_raises(ft_grey, np.array([42]))

# load the image
array = ft_load("landscape.jpg")

# should transform the arrays
# should print the pixels
# should display the images
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
print(ft_grey(array))
print(ft_invert.__doc__)
