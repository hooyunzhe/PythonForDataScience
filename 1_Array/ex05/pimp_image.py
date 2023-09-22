import numpy as np
import matplotlib.pyplot as plt


def ft_invert(image_array: np.ndarray) -> np.ndarray:
    """
    A function that inverts the colors of the given 3D array
    representing an image's pixels in RGB format, then
    prints its pixels and displays the transformed image

    Arguments:
        image_array (np.ndarray): 3D array to be inverted

    Returns:
        the transformed array
    """

    # make sure image_array is a numpy array of 3 dimensions
    assert type(image_array) is np.ndarray, "image_array must be a numpy array"
    assert image_array.ndim == 3, "image_array must be a 3D numpy array"

    # invert the values by subtracting from the max value of RGB
    inverted_image_array = 255 - image_array

    # print the pixels
    print(image_array)

    # display the transformed image
    plt.imshow(inverted_image_array)
    plt.show()

    # return the transformed array
    return inverted_image_array


def ft_red(image_array: np.ndarray) -> np.ndarray:
    """
    A function that preserves only the red colors of the given 3D array
    representing an image's pixels in RGB format

    Arguments:
        image_array (np.ndarray): 3D array to be transformed

    Returns:
        the transformed array
    """

    # make sure image_array is a numpy array of 3 dimensions
    assert type(image_array) is np.ndarray, "image_array must be a numpy array"
    assert image_array.ndim == 3, "image_array must be a 3D numpy array"

    # preserve only red colors by setting other color values to 0
    transformed_image_array = image_array * [1, 0, 0]

    # print the pixels
    print(image_array)

    # display the transformed image
    plt.imshow(transformed_image_array)
    plt.show()

    # return the transformed array
    return transformed_image_array


def ft_green(image_array: np.ndarray) -> np.ndarray:
    """
    A function that preserves only the green colors of the given 3D array
    representing an image's pixels in RGB format

    Arguments:
        image_array (np.ndarray): 3D array to be transformed

    Returns:
        the transformed array
    """

    # make sure image_array is a numpy array of 3 dimensions
    assert type(image_array) is np.ndarray, "image_array must be a numpy array"
    assert image_array.ndim == 3, "image_array must be a 3D numpy array"

    # copy the array
    transformed_image_array = np.copy(image_array)

    # preserve only green colors by setting other color values to 0
    transformed_image_array[..., 0] = (
        transformed_image_array[..., 0] - transformed_image_array[..., 0])
    transformed_image_array[..., 2] = (
        transformed_image_array[..., 2] - transformed_image_array[..., 2])

    # print the pixels
    print(image_array)

    # display the transformed image
    plt.imshow(transformed_image_array)
    plt.show()

    # return the transformed array
    return transformed_image_array


def ft_blue(image_array: np.ndarray) -> np.ndarray:
    """
    A function that preserves only the blue colors of the given 3D array
    representing an image's pixels in RGB format

    Arguments:
        image_array (np.ndarray): 3D array to be transformed

    Returns:
        the transformed array
    """

    # make sure image_array is a numpy array of 3 dimensions
    assert type(image_array) is np.ndarray, "image_array must be a numpy array"
    assert image_array.ndim == 3, "image_array must be a 3D numpy array"

    # copy the array
    transformed_image_array = np.copy(image_array)

    # preserve only blue colors by setting other color values to 0
    transformed_image_array[..., 0] = 0
    transformed_image_array[..., 1] = 0

    # print the pixels
    print(image_array)

    # display the transformed image
    plt.imshow(transformed_image_array)
    plt.show()

    # return the transformed array
    return transformed_image_array


def ft_grey(image_array: np.ndarray) -> np.ndarray:
    """
    A function that transforms the given 3D array
    representing an image's pixels in RGB format to greyscale

    Arguments:
        image_array (np.ndarray): 3D array to be transformed

    Returns:
        the transformed array
    """

    # make sure image_array is a numpy array of 3 dimensions
    assert type(image_array) is np.ndarray, "image_array must be a numpy array"
    assert image_array.ndim == 3, "image_array must be a 3D numpy array"

    # copy the array
    transformed_image_array = np.copy(image_array)

    # transform to grayscale by setting all color values
    # to the average RGB value of each pixel
    grayscale_rgb = transformed_image_array.mean(axis=2, dtype=np.int64)
    transformed_image_array[:, :, 0] = grayscale_rgb
    transformed_image_array[:, :, 1] = grayscale_rgb
    transformed_image_array[:, :, 2] = grayscale_rgb

    # print the pixels
    print(image_array)

    # display the transformed image
    plt.imshow(transformed_image_array)
    plt.show()

    # return the transformed array
    return transformed_image_array
