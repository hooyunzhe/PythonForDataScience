from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the image "animal.jpeg",
    prints its information, zooms and displays the image as grayscale
    """

    # load the image
    image_array = ft_load("animal.jpeg")

    # zoom the image by slicing the array
    # only keep the R pixel for grayscale
    zoomed_image_array = image_array[100:500, 450:850, 0:1]

    # print the new shape and its pixels
    print("New shape after slicing: (400, 400, 1) or (400, 400)")
    print(zoomed_image_array)

    # display the image as grayscale by setting up the colormapping
    plt.imshow(zoomed_image_array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
