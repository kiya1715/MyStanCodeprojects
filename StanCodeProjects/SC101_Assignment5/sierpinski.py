"""
File: sierpinski.py
Name: Karen Chang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draw a sierpinski triangle on GWindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	This function will draw a sierpinski triangle on GWindow with recursion.

	:param order: int, How many orders the sierpinski triangle is
	:param length: int, The length of order 1 Sierpinski Triangle
	:param upper_left_x: int, The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: int, The upper left y coordinate of order 1 Sierpinski Triangle
	:return: The sierpinski triangle on GWindow
	"""

	# Base case
	if order == 0:
		pass

	# when order is 1, the function will only draw a triangle
	elif order == 1:
		draw_triangle(length, upper_left_x, upper_left_y)

	else:
		# draw the triangle
		draw_triangle(length, upper_left_x, upper_left_y)

		# upper_left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		# upper_right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)

		# lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+length/2*0.866)


def draw_triangle(length, upper_left_x, upper_left_y):
	"""
	This function will draw a inverted equilateral triangle which the upper left point placed at pointed position.

	:param length: int, The length of the inverted equilateral triangle
	:param upper_left_x: int, The upper left x coordinate of the inverted equilateral triangle
	:param upper_left_y: int, The upper left y coordinate of the inverted equilateral triangle
	:return: draw a equilateral Triangle on the pointed position.
	"""

	# The upper line of the inverted equilateral triangle
	line1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
	window.add(line1)

	# The left line of the inverted equilateral triangle
	line2 = GLine(upper_left_x, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
	window.add(line2)

	# The right line of the inverted equilateral triangle
	line3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
	window.add(line3)


if __name__ == '__main__':
	main()