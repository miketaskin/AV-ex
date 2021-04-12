import os
import pathlib
import sys
import image_grayscale
from PIL import Image

from validation import isint

THRESHOLDING_MODE = "1"


def global_thresholding(image, threshold):
    if image.mode != image_grayscale.GRAYSCALE_MODE:
        raise ValueError

    if not isint(threshold) or threshold < 0 or threshold > 255:
        raise ValueError

    result = Image.new(THRESHOLDING_MODE, image.size)

    for x in range(image.width):
        for y in range(image.height):
            result.putpixel((x, y), image.getpixel((x, y)) > threshold)

    return result


def main(image_path_str):
    working_dir_path = ''
    if not os.path.isabs(image_path_str):
        working_dir_path = pathlib.Path().absolute()
    full_image_path = os.path.join(working_dir_path, image_path_str)
    image = image_grayscale.mean_grayscale(Image.open(full_image_path).convert("RGB"))
    global_thresholding(image, 140).save("imageBW.png")


if __name__ == '__main__':
    main(sys.argv[1])
