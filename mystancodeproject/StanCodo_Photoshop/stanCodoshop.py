"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((red - pixel.red) ** 2 + (blue - pixel.blue) ** 2 + (green - pixel.green) ** 2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_red = 0
    sum_blue = 0
    sum_green = 0

    for i in range(len(pixels)):
        img = pixels[i]
        sum_red += img.red
        sum_blue += img.blue
        sum_green += img.green

    avg_red = sum_red // len(pixels)
    avg_blue = sum_blue // len(pixels)
    avg_green = sum_green // len(pixels)

    color_lst = [avg_red, avg_green, avg_blue]
    return color_lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_value = get_average(pixels)
    shortest_distance_pixel = []
    minimum = 1000000

    for i in range(len(pixels)):
        shortest_distance = get_pixel_dist(pixels[i], avg_value[0], avg_value[1], avg_value[2])
        if shortest_distance < minimum:
            shortest_distance_pixel = pixels[i]

    return shortest_distance_pixel


def solve(images):
    """
    Given a list of image objects, compute and disply a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    #  針對每個pixel(x, y)進行運作的迴圈。
    for x in range(width):
        for y in range(height):

            # 儲存每張照片相同pixel(x,y)的序列之初始值。
            img_pixels_lst = []

            # 執行每張照片相同pixel(x,y)的迴圈。
            for i in range(len(images)):

                # 將每張照片之相同位置pixel(x,y)丟入序列。
                img_pixels_lst.append(images[i].get_pixel(x, y))

            # 將pixels序列丟入get_best_pixel，尋找最佳pixel。
            best_pixel = get_best_pixel(img_pixels_lst)

            # 抓取空白frame之pixel,將該RGB色調改為best_pixel箱子內之色調。
            clear_photo = result.get_pixel(x, y)
            clear_photo.red = best_pixel.red
            clear_photo.blue = best_pixel.blue
            clear_photo.green = best_pixel.green

        # print(img_pixels_lst[0],img_pixels_lst[1],img_pixels_lst[2])

    # Milestone 1
    """green_im = SimpleImage.blank(20, 20, 'green')
    green_pixel = green_im.get_pixel(0, 0)
    print(get_pixel_dist(green_pixel, 5, 255, 10))"""

    # Milestone 2
    """green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))"""

    # Milestone 3
    """green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    print(best1.red, best1.green, best1.blue)"""

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
