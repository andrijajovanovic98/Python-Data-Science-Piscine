import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def transpose(matrix):
    """Transporing manually"""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    return transposed


def print_before(img_array_gray):
    """Printing syntax"""
    print(f"The shape of image is: {img_array_gray.shape}")
    print("[[", end="")
    print(img_array_gray[0, 0])
    print("  " + str(img_array_gray[1, 0].tolist()))
    print("  " + str(img_array_gray[2, 0].tolist()))
    print("   ...")

    print("  " + str(img_array_gray[-3, 0].tolist()))
    print("  " + str(img_array_gray[-2, 0].tolist()))
    print("  " + str(img_array_gray[-1, 0].tolist()), end="")
    print("]]")


def print_after(img_array_transposed):
    """Printing syntax"""
    print(f"New shape after Transpose: {img_array_transposed.shape}")

    print("[[", end="")
    print(" ".join(map(str, img_array_transposed[0, :3])), "...", " ".join(
        map(str, img_array_transposed[0, -3:])), end="")
    print("]")

    print(" ...")

    print("[", end="")
    print(" ".join(map(str, img_array_transposed[-1, :3])), "...", " ".join(
        map(str, img_array_transposed[-1, -3:])), end="")
    print("]]")


def main():
    """The main function"""
    image_array = ft_load("animal.jpeg")

    if image_array is None:
        print("Image not found")
        return

    height, width, _ = image_array.shape

    if height < 400 or width < 400:
        print("Image too small")
        return

    size = 400

    y_start = (height - size) // 2
    y_end = (height + size) // 2
    x_start = (width - size) // 2
    x_end = (width + size) // 2

    img_array_zoomed = image_array[y_start:y_end, x_start:x_end]
    img_gray = Image.fromarray(img_array_zoomed).convert("L")
    img_array_gray = np.array(img_gray)
    img_array_gray = np.expand_dims(img_array_gray, axis=-1)

    print_before(img_array_gray)
    img_array_transposed = np.array(
        transpose(img_array_gray[:, :, 0].tolist()))

    print_after(img_array_transposed)

    fig, ax = plt.subplots()

    ax.imshow(img_array_transposed, cmap="gray")
    ax.set_xticks(np.arange(0, size, 50))
    ax.set_yticks(np.arange(0, size, 50))
    ax.set_title("Sliced image")

    plt.show()


if __name__ == "__main__":
    main()
