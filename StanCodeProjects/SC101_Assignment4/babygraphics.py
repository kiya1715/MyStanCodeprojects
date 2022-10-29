"""
File: babygraphics.py
Name: Karen Chang
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
    gap = int((width-GRAPH_MARGIN_SIZE*2)/len(YEARS))
    x_coordinate = int(GRAPH_MARGIN_SIZE + gap*(year_index-1))

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Top_line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # Button_line
    button_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    canvas.create_line(GRAPH_MARGIN_SIZE, button_y, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, button_y)

    # Canvas lines and years
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i+1)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, button_y, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # y_gap is the gap of each rank
    y_gap = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000

    # n is which color in the COLOR list be shown for the information of the name user searched
    n = 0

    # confirming the information of the name user searched
    for match_name in lookup_names:
        if match_name in name_data:

            # select the color
            color = COLORS[n]
            if n == len(COLORS) - 1:
                n = 0
            else:
                n += 1

            # get the x coordinate
            for i in range(len(YEARS)):
                year = str(YEARS[i])
                x = get_x_coordinate(CANVAS_WIDTH, i+1)

                # get the y coordinate and rank information
                # the rank of the year is in top 1000
                if year in name_data[match_name]:
                    rank = name_data[match_name][year]
                    y = GRAPH_MARGIN_SIZE + y_gap*int(rank)
                    show_text = match_name + rank

                # the rank of the year is out of top 1000
                else:
                    y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    show_text = match_name + "*"

                # start to draw the line from the second year in the canvas
                if i != 0:
                    canvas.create_line(pre_x, pre_y, x, y, width=LINE_WIDTH, fill=color)

                # add the text about the name and rank information
                canvas.create_text(x + TEXT_DX, y, text=show_text, anchor=tkinter.SW, fill=color)
                pre_x = x
                pre_y = y


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
