"""
File: blur.py
Name:Jason Tsai (智翔)
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)
            total_red = 0                                       # 定義total_red箱子初始值為0。
            total_blue = 0                                      # 定義total_blue箱子初始值為0。
            total_green = 0                                     # 定義total_green箱子初始值為0。
            total_num = 0                                       # 定義total_num箱子初始值為0。
            if x == 0:                                          # 判斷並定義圖像X軸最左側(0, 0)的極端狀況。
                row_left = x
            else:
                row_left = x - 1
            if y == 0:                                          # 判斷並定義圖像y軸最上方(0, 0)的極端狀況。
                column_upper = y
            else:
                column_upper = y - 1
            if x == (img.width-1):                              # 判斷並定義圖像X軸最右側(img.width, 0)的極端狀況。
                row_right = x
            else:
                row_right = x + 1
            if y == (img.height-1):                             # 判斷並定義圖像y軸最下方(0, img.height)的極端狀況。
                column_down = y
            else:
                column_down = y + 1

            for r in range(row_left, row_right+1):              # 開始執行RGB Value的計算，帶入迴圈，範圍為X軸pixel個數。
                for c in range(column_upper, column_down+1):    # 開始執行RGB Value的計算，帶入迴圈，範圍為Y軸pixel個數。
                    total_red += img.get_pixel(r, c).red        # 開始累加total_red箱子。
                    total_blue += img.get_pixel(r, c).blue      # 開始累加total_blue箱子。
                    total_green += img.get_pixel(r, c).green    # 開始累加total_green箱子。
                    total_num += 1                              # 開始累計需要平均的個數。

            pixel.red = total_red / total_num                   # 進行新pixel.red的平均數計算。
            pixel.green = total_green / total_num               # 進行新pixel.blue的平均數計算。
            pixel.blue = total_blue / total_num                 # 進行新pixel.green的平均數計算。

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
