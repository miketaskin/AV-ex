import os
import pathlib
import sys
from PIL import Image


def rotate_image_on_180(image):
    # image.width-ширина
    # image.height-высота
    # image.getpixel((x,y))
    # image.putpixel((x,y),pixelvalue)-устанавливает
    result = Image.new(image.mode, image.size)
    for x in range(image.width):
        for y in range(image.height):
            result.putpixel((x, y), image.getpixel((image.width - 1 - x, image.height - 1 - y)))
    return result


def mirror_image(image):
    result = Image.new(image.mode, image.size)
    for x in range(image.width):
        for y in range(image.height):
            result.putpixel((x, y), image.getpixel((image.width - 1 - x, y)))
    return result


def main(image_path_str):
    working_dir_path = ''
    if not os.path.isabs(image_path_str):
        working_dir_path = pathlib.Path().absolute()
    full_image_path = os.path.join(working_dir_path, image_path_str)
    image = Image.open(full_image_path)
    rotate_image_on_180(image).show()
    mirror_image(image).show()


if __name__ == '__main__':
    main(sys.argv[1])
