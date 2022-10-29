"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

class BreakoutGraphics:
    """
    This class helps to create a Breakout clone games.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-PADDLE_WIDTH)/2, y=window_height-PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.ball_acting = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.moving_ball)

        # Draw bricks
        y = BRICK_OFFSET

        # Draw a 10X10 bricks in the top area of the window and each 2 rows has different colors.
        for i in range(BRICK_COLS):
            x = 0
            if i < 2:
                color = "mediumblue"
            elif i == 2 or i == 3:
                color = "cornflowerblue"
            elif i == 4 or i == 5:
                color = "skyblue"
            elif i == 6 or i == 7:
                color = "powderblue"
            else:
                color = "turquoise"

            for j in range(BRICK_ROWS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.color = color
                brick.filled = True
                brick.fill_color = color
                self.window.add(brick, x=x, y=y)
                x += (BRICK_WIDTH+BRICK_SPACING)

            y += (BRICK_HEIGHT + BRICK_SPACING)

    def paddle_move(self, event):
        """
        This method let paddle move horizontally between the window.
        """
        if event.x < PADDLE_WIDTH:
            self.paddle.x = 0
        elif event.x > self.window.width-PADDLE_WIDTH:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        else:
            self.paddle.x = event.x - PADDLE_WIDTH/2

    def moving_ball(self, event):
        """
        This method confirm the ball's acting when user click.
        The default status of the ball is False when it be placed at the meddle of window.
        And if the ball is not moving when user click, it will let ball start to move and change status to True.
        """
        self.ball_acting = True

    def setup_velocity(self):
        """
        The method is setting the speed and random direction of the ball.
        """
        if self.ball_acting is True:
            self.__dy = INITIAL_Y_SPEED                   # The vertical speed which is stable
            self.__dx = random.randint(1, MAX_X_SPEED)    # The random speed of horizontal moving
            if random.random() > 0.5:                     # The random direction of the ball
                self.__dx = -self.__dx

    def get_dx(self):
        """
        This method let user side can use the horizontal speed which is set in 'setup_velocity' method
        :return: The horizontal speed
        """
        return self.__dx

    def get_dy(self):
        """
        This method let user side can use the vertical speed which is set in 'setup_velocity' method
        :return: The vertical speed
        """
        return self.__dy

    def set_vy(self, new_vy):
        """
        This method will change the value of vertical speed and direction of the ball
        :return: New vertical speed and direction
        """
        self.__dy = new_vy

    def confirm_collision(self):
        """
        The method confirms whether the ball hit the objects (bricks and paddle) in the window.
        If the ball hits the bricks, the brick will be removed and the ball will rebound.
        If the ball his  the paddle, the ball will rebound only.
        """
        # To avoid the ball bounce in the paddle area
        hit_paddle = False

        # Confirm each corner of the ball to see if it hit the object or not
        for i in range(4):
            bx = self.ball.x
            by = self.ball.y

            if i % 2 != 0:
                bx = self.ball.x+BALL_RADIUS*2
            elif i > 1:
                by = self.ball.y+BALL_RADIUS*2

            # The ball hits objects
            if self.window.get_object_at(bx, by):

                # If the ball hits bricks
                if by < self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT:
                    brick = self.window.get_object_at(bx, by)
                    self.window.remove(brick)
                    return True
                    break

                # if the ball hits the paddle
                else:
                    if self.__dy > 0:
                        return True
                    else:
                        return False

    def reset(self):
        """
        This method place the ball at the middle of the window and the ball is not moving.
        """
        self.ball_acting = False
        self.ball.x = self.window.width/2-BALL_RADIUS
        self.ball.y = self.window.height/2-BALL_RADIUS

    def confirm_bricks(self):
        """
        This method confirms whether the bricks are all removed or not in the window.
        If the bricks are all removed, it will stop the game.
        """
        x = 0              # The x value of brick's position which starts from o
        y = BRICK_OFFSET   # The y value of brick's position which starts from 'BRICK_OFFSET'

        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                if self.window.get_object_at(x, y) is not None:
                    return False
                else:
                    x += (BRICK_WIDTH + BRICK_SPACING)

            y += (BRICK_HEIGHT + BRICK_SPACING)
        return True

    def win(self):
        """
        This method remove the ball in the window and will show "You Win!" if the bricks are all removed.
        """
        self.window.remove(self.ball)
        congratulation = GLabel('You Win!')
        congratulation.font = '-60'
        self.window.add(congratulation, x=(self.window.width-congratulation.width)/2, y=(self.window.height-congratulation.height)/2)
