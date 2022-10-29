"""
File: bouncing_ball.py
Name: Karen.chang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# The window for use's click
window = GWindow(800, 500, title='bouncing_ball.py')

# The circle for bouncing
oval = GOval(SIZE, SIZE)

# 'click' is the switch for the react of click during bouncing
click = True

# 'r' is the switch for the react of the bouncing
r = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # The status of the ball in the beginning
    set_ball()

    # The result of user's click
    onmouseclicked(falling_ball)


def set_ball():
    """
    This function will create a circle which is at (START_X,START_Y) in the window
    """
    oval.filled = True
    window.add(oval, x=START_X, y=START_Y)


def falling_ball(mouse):
    """
    When the circle is at (START_X,START_Y), the circle will start to bounce if user click.
    The circle will rebound when it hit the bottom of the window and get lower until it goes outside of the window.
    During the circle's bouncing or after three times of the bouncing, there is no reaction to user's click.
    """
    global r, click
    vy = 0
    y1 = START_Y

    # The first three times of the bouncing of the circle
    while r < 3:

        # The reaction to user's click when the circle is not bouncing
        if click:
            click = False
            while oval.x <= window.width:
                oval.move(VX, vy)
                if oval.y >= window.height:
                    vy = -vy*REDUCE
                    y1 *= REDUCE
                elif oval.y < y1:
                    vy = -vy
                else:
                    vy += GRAVITY
                pause(DELAY)
            set_ball()
            r += 1
            click = True
            return

        # When the circle is bouncing, there is not reaction to user's click
        else:
            return


if __name__ == "__main__":
    main()
