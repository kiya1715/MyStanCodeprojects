"""
File: blur.py
Name: Karen Chang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return new_img: SimpleImage, Blurred image
    Function: Blur the imported image
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    # To create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # To get pixel of new_img at x,y
            new_pixel = new_img.get_pixel(x, y)

            num = 0
            red = 0
            green = 0
            blue = 0

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            # Define the start number of i
            if x == 0:
                sj = 0
            else:
                sj = -1

            # Define the end number of i
            if x == img.width - 1:
                w = 1
            else:
                w = 2

            # Define the start number of j
            if y == 0:
                si = 0
            else:
                si = -1

            # Define the end number of j
            if y == new_img.height - 1:
                h = 1
            else:
                h = 2

            # Add up RGB values individually
            for i in range(si, h):
                for j in range(sj, w):
                    red += img.get_pixel(x+j, y+i).red
                    green += img.get_pixel(x+j, y+i).green
                    blue += img.get_pixel(x+j, y+i).blue
                    num += 1

            # Get new pixel
            new_pixel.red = red/num
            new_pixel.green = green/num
            new_pixel.blue = blue/num

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
