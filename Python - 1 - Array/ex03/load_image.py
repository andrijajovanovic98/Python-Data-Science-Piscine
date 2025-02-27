import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image, prints its format
    and shape and return numpy array in  RGB format."""
    try:

        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Error: Only JPG and JPEG formats are supported.")

        img = img.convert("RGB")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print("Error: File not Found")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occured: {e}")
