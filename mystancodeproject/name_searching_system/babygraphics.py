"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    chart_line_width = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)             # 計算每年分之間的直線寬度。
    chart_line_width_x = GRAPH_MARGIN_SIZE + year_index * chart_line_width      # 計算每年分的x軸座標。
    return chart_line_width_x                                                   # 回傳計算後座標值。


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # 圖表最上方的橫線。
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # 圖表最下方的橫線。
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # 直線與年份文字執行迴圈。
    for i in range(len(YEARS)):

        # 直線製作。
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)

        # print出年分wording。
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):

    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i in range(len(lookup_names)):                                                  # 執行迴圈。
        for j in range(len(YEARS) - 1):                                                 # 執行迴圈。
            key_year = YEARS[j]                                                         # 讀取年分。
            key_year_2 = YEARS[j + 1]                                                   # 讀取下個年分。

            rank_value = name_data.get(lookup_names[i]).get(str(key_year))              # 取得年份排名。
            rank_value_2 = name_data.get(lookup_names[i]).get(str(key_year_2))          # 取得下個年份排名。

            if rank_value is None or int(rank_value) > 1000:                            # 當排名超過1000或不存在時執行
                y_start = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE                             # 起始點y軸計算。
                rank_value = '--'                                                       # 超過或不存在時以'--'替代。
            else:                                                                       # 當排名在1000以內時執行
                y_start = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) * int(rank_value) / 1000 + GRAPH_MARGIN_SIZE

            if rank_value_2 is None or int(rank_value_2) > 1000:                        # 當排名超過1000或不存在時執行
                y_end = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE                               # 起始點y軸計算。
            else:                                                                       # 當排名在1000以內時執行
                y_end = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) * int(rank_value_2) / 1000 + GRAPH_MARGIN_SIZE

            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), y_start,
                               get_x_coordinate(CANVAS_WIDTH, j + 1), y_end,
                               width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])          # 在兩個年度之間畫線。

            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j), y_start - TEXT_DX, fill=COLORS[i % len(COLORS)],
                               text='(' + lookup_names[i] + ' , ' + rank_value + ')', anchor=tkinter.SW)    # 座標註記。


    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    key:Kylie Nicholas Sonja
    """
# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
