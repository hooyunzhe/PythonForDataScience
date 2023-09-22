from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the image "animal.jpeg",
    crops a square, prints its information,
    rotates and displays the image
    """

    # load the image
    image_array = ft_load("animal.jpeg")

    # crop the image by slicing the array
    # only keep the R pixel for grayscale
    cropped_image_array = image_array[100:500, 450:850, 0:1]

    # print the shape
    print("The shape of image is: (400, 400, 1) or (400, 400)")
    print(cropped_image_array)

    # rotate the image by transposing the array
    rotated_image_array = [cropped_image_array[:, i, 0] for i in range(400)]

    # convert the array to a numpy array
    rotated_image_array = np.array(rotated_image_array)

    # print the new shape
    print("New shape after Transpose: (400, 400)")
    print(rotated_image_array)

    # display the image as grayscale by setting up the colormapping
    plt.imshow(rotated_image_array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
