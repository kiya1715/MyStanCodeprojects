"""
File: draw_line.py
Name: Karen Chang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# The size of the circle at user's first click
SIZE = 10

# The window for the click
window = GWindow()

# 'click' is how many times user clicked
click = 0

# 'x1' and 'y1' is the position of user's odd click
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    On user's odd click, it will create a circle which the center of the circle is at the position user clicked
    On user's even click it will remove the circle on the window
    and create a line starts at the position of user's odd clicked, ends at the position of user's even clicked.
    """
    global click, x1, y1
    # Calculate how many times user clicked
    click += 1

    # User's odd click
    if click % 2 != 0:
        circle = GOval(SIZE, SIZE)
        window.add(circle, x=mouse.x - circle.width / 2, y=mouse.y - circle.height / 2)
        x1 = mouse.x
        y1 = mouse.y

    # User's even click
    else:
        circle = window.get_object_at(x1, y1)
        window.remove(circle)
        line = GLine(x1, y1, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
