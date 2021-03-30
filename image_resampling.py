import os
import pathlib
import sys
from PIL import Image


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def image_upsampling_closest_neighbour(image, n):
    if not isint(n) or n <= 0:
        raise ValueError
    result = Image.new(image.mode, (image.width * n, image.height * n))
    for x in range(result.width):
        for y in range(result.height):
            result.putpixel((x, y), image.getpixel((x // n, y // n,)))
    return result


def image_downsampling_decimation(image, n):
    if not isint(n) or n <= 0:
        raise ValueError

    result = Image.new(image.mode, (image.width // n, image.height // n))

    for x in range(result.width):
        for y in range(result.height):
            result.putpixel((x, y), image.getpixel((x * n, y * n)))

    return result


def image_upsampling_interpolation(image, n):
    if not isint(n) or n <= 0:
        raise ValueError

    result = Image.new(image.mode, (image.width * n, image.height * n))

    for x in range(result.width - n):
        for y in range(result.height - n):
            if x % n == 0 and y % n == 0:
                result.putpixel((x, y), image.getpixel((x // n, y // n)))
            else:
                left_upper_color = image.getpixel((x // n, y // n))
                right_upper_color = image.getpixel((x // n + 1, y // n))
                t = (x - x // n * n) / ((x // n + 1 - x // n) * n)

                upper_line_color = rgb_lerp(left_upper_color, right_upper_color, t)

                left_lower_color = image.getpixel((x // n, y // n + 1))
                right_lower_color = image.getpixel((x // n + 1, y // n + 1))
                t = (x - x // n * n) / ((x // n + 1 - x // n) * n)

                lower_line_color = rgb_lerp(left_lower_color, right_lower_color, t)

                t = (y - y // n * n) / ((y // n + 1 - y // n) * n)
                result_color = rgb_lerp(upper_line_color, lower_line_color, t)

                result.putpixel((x, y), result_color)

    return result


def rgb_lerp(color1, color2, t):
    r = int(round((color2[0] - color1[0]) * t + color1[0]))
    g = int(round((color2[1] - color1[1]) * t + color1[1]))
    b = int(round((color2[2] - color1[2]) * t + color1[2]))

    return r, g, b


def main(image_path_str):
    working_dir_path = ''
    if not os.path.isabs(image_path_str):
        working_dir_path = pathlib.Path().absolute()
    full_image_path = os.path.join(working_dir_path, image_path_str)
    image = Image.open(full_image_path)
    image_upsampling_closest_neighbour(image, 3).save("result.png")
    # image_downsampling_decimation(image, 3).save("result1.png")
    image_upsampling_interpolation(image, 3).save("result1.png")


if __name__ == '__main__':
    main(sys.argv[1])
