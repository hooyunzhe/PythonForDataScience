import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    A function that opens an image at the given path
    and returns it as a numpy array

    Arguments:
        path (str): path of image to load

    Returns:
        a 3D array representing the image's pixels
    """

    # make sure path is a string
    assert type(path) is str, "path must be a string"

    # open the image
    img = Image.open(path)

    # convert the image to a numpy array
    img_arr = np.array(img)

    # print the shape of the array
    print(f"The shape of image is: {img_arr.shape}")

    # return the converted image
    return img_arr
