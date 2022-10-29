"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from extention_breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This is a Breakout clone games.
    In the beginning, user can see a ball in the meddle of window and bricks in the top area
    and a paddle in the bottom area. User can get three chances to remove all the bricks by the moving ball.
    The game will be ended only if user removed all bricks or run out of three chances.
    """

    # Create the initial screen
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    life = NUM_LIVES
    graphics.set_hp(life)

    # the setting of the game
    while True:
        pause(FRAME_RATE)
        graphics.setup_velocity()
        vx = graphics.get_dx()
        vy = graphics.get_dy()

        # if user has not run out of three chances and the ball is moving
        while life != 0 and graphics.ball_acting is True:
            pause(FRAME_RATE)
            graphics.ball.move(vx, vy)

            # When the ball hit the bottom of the window
            if graphics.ball.y >= graphics.window.height-graphics.ball.height:
                life -= 1
                graphics.reset()
                graphics.set_hp(life)

            # When the ball hit objects in the window or the edge of the window
            else:
                if graphics.ball.x < 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
                    vx = -vx
                elif graphics.ball.y < 0 or graphics.ball.y+graphics.ball.height > graphics.window.height:
                    vy = -vy

            # When the ball hit bricks or paddle in the window
            con = graphics.confirm_collision()
            if con:
                graphics.set_vy(-vy)
                vy = graphics.get_dy()

            # confirming whether the bricks are all removed or not
            check = graphics.confirm_bricks()
            if check:
                graphics.win()
                break

        # When user used all chances but can not remove all bricks
        if life == 0:
            graphics.lose()

if __name__ == '__main__':
    main()

