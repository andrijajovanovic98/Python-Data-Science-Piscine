import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def print_before(image_array):
    """Print syntax"""

    print("[[", end="")
    print(*image_array[:1, :3].reshape(-1, 3), sep="\n")
    print("    ...   ")
    print(*image_array[-1:, -3:].reshape(-1, 3), sep="\n", end="")
    print("]]")


def print_after_zoom(img_array_zoomed):
    """Print syntax"""

    print(f"New shape after slicing: {img_array_zoomed.shape}")

    print("[[", end="")
    print(f"[{img_array_zoomed[0, 0]}]")
    for row in img_array_zoomed[1:3, :1]:
        print(f"  [{row[0]}]")
    print("  ...")
    for row in img_array_zoomed[-3:-1, :1]:
        print(f"  [{row[0]}]")
    print(f"  [{img_array_zoomed[-1, 0]}", end="")
    print("]]]")


def main():
    """The main function"""

    image_array = ft_load("animal.jpeg")
    if image_array is None:
        return

    height, width, _ = image_array.shape

    if height < 400 or width < 400:
        print("Image too small")
        return

    print_before(image_array)

    size = 400
    y_start = (height - size) // 2
    y_end = (height + size) // 2
    x_start = (width - size) // 2
    x_end = (width + size) // 2

    img_array_zoomed = image_array[y_start:y_end, x_start:x_end]

    img_gray = Image.fromarray(img_array_zoomed).convert("L")
    img_array_gray = np.array(img_gray)
    img_array_gray = np.expand_dims(img_array_gray, axis=-1)
    img_array_zoomed = np.expand_dims(img_array_gray, axis=-1)
    img_array_zoomed = np.squeeze(img_array_zoomed)
    print_after_zoom(img_array_zoomed)

    fig, ax = plt.subplots()

    ax.imshow(img_gray, cmap="gray")
    ax.set_xticks(np.arange(0, size, 50))
    ax.set_yticks(np.arange(0, size, 50))
    ax.set_title("Sliced image")

    plt.show()


if __name__ == "__main__":
    main()
