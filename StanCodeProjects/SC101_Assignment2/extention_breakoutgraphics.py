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

        # The score of brick
        self.__score = 0

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

        # Set the scoreboard in the window
        self.scoreboard = GLabel("Score: " + str(self.__score))
        self.scoreboard.font = '-15'
        self.window.add(self.scoreboard, x=2, y=30)

        # Create a label for showing how many chances user have
        self.__hp = GLabel('\u2764')

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
        :return: The horizontal speed
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

        # Confirm each corner of the ball to see if it hit the object or not
        for i in range(4):
            bx = self.ball.x
            by = self.ball.y

            if i % 2 != 0:
                bx = self.ball.x+BALL_RADIUS*2
            elif i > 1:
                by = self.ball.y+BALL_RADIUS*2

            # The ball hits objects
            ob = self.window.get_object_at(bx, by)
            if ob is not None and ob is not self.scoreboard and ob is not self.__hp:

                # If the ball hits bricks
                if by < self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT:
                    brick = self.window.get_object_at(bx, by)
                    self.s_calculation(bx, by)
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
        congratulation.font = '-50'
        congratulation.color = 'red'
        self.window.add(congratulation, x=(self.window.width-congratulation.width)/2, y=(self.window.height-congratulation.height)/2)

    def lose(self):
        """
        If user used all chances but can not remove all bricks, this method will show
        'Sorry, you lose :(' in the window
        """
        lose_label = GLabel('Sorry, you lose :(')
        lose_label.font = '-45'
        lose_label.color = 'darksalmon'
        self.window.add(lose_label, x=(self.window.width - lose_label.width) / 2,
                        y=(self.window.height - lose_label.height) / 2)

    def s_calculation(self, bx, by):
        """
        This method calculate the score of brick which be hit by the ball.
        If the brick which is higher, the score is higher as well.
        """

        line1 = BRICK_OFFSET+BRICK_HEIGHT*2+BRICK_SPACING*1.5
        line2 = line1+BRICK_HEIGHT*2+BRICK_SPACING*2
        line3 = line2+BRICK_HEIGHT*2+BRICK_SPACING*2
        line4 = line3+BRICK_HEIGHT*2+BRICK_SPACING*2
        line5 = line4+BRICK_HEIGHT*2+BRICK_SPACING*2

        # setting of the score
        if by < line1:
            self.__score += 50
        elif line1 < by < line2:
            self.__score += 40
        elif line2 < by < line3:
            self.__score += 30
        elif line3 < by < line4:
            self.__score += 20
        elif line4 < by < line5:
            self.__score += 10

        # Show the current total score in the window
        self.scoreboard.text = ("Score: " + str(self.__score))

    def set_hp(self, life):
        """
        This method show how many chances user have by the heart emoji ('\u2764')
        """
        # Set the detail of the heart emoji
        self.__hp.font = '-25'
        self.__hp.color = 'tomato'
        hpx = self.window.width - 30 * life

        # Add the heart emoji in the window
        self.__hp.text = '\u2764'*life
        self.window.add(self.__hp, x=hpx, y=40)
