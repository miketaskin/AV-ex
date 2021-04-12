import os
import pathlib
import sys
from PIL import Image
GRAYSCALE_MODE = "L"


def mean_grayscale(image):
    result = Image.new(GRAYSCALE_MODE, image.size)
    for x in range(image.width):
        for y in range(image.height):
            result.putpixel((x, y), int(round(sum(image.getpixel((x, y))) / 3)))

    return result


def photoshop_grayscale(image):
    result = Image.new(GRAYSCALE_MODE, image.size)
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.getpixel((x, y))
            result.putpixel((x, y), int(round(0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2])))

    return result









def main(image_path_str):
    working_dir_path = ''
    if not os.path.isabs(image_path_str):
        working_dir_path = pathlib.Path().absolute()
    full_image_path = os.path.join(working_dir_path, image_path_str)
    image = Image.open(full_image_path).convert("RGB")
    #mean_grayscale(image).save("image1.png")
    photoshop_grayscale(image).save("image2.png")


if __name__ == '__main__':
    main(sys.argv[1])
