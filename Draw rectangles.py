import random
from graphics import *

# Returns the first mouse click at a point outside of the message bar. This
# prevents rectangles from being drawn on top of the message bar.
def getValidMouse(win):
    point = Point(0, 330)
    while point.getY() >= 330:
        point = win.getMouse()
    return point

# Returns the area and perimeter of a rectangle.
def getRectInfo(rect):
    corner1 = rect.getP1()
    corner2 = rect.getP2()

    intLength = abs(corner1.getX() - corner2.getX())
    intWidth = abs(corner1.getY() - corner2.getY())

    intArea = intLength * intWidth
    intPerimeter = 2 * (intLength + intWidth)
    return intArea, intPerimeter

# Draws and returns a message bar at the bottom of the window.
def drawMessageBar(win):
    bar = Rectangle(Point(1, 330), Point(352, 352))
    bar.setFill("#eee")
    bar.setOutline("#bbb")
    bar.draw(win)
    
    message = Text(Point(175, 341), "Keep clicking to draw rectangles.")
    message.setSize(11)
    message.draw(win)
    return message

# Draws and returns a rectangle with points determined by the user.
def drawUserRectangle(win, strFillColor, strOutlineColor):

    # Wait for the user to click twice to determine two opposite corners of the
    # rectangle.
    corner1 = getValidMouse(win)
    corner1.draw(win)
    corner2 = getValidMouse(win)
    corner1.undraw()

    # Draw the rectangle.
    rect = Rectangle(corner1, corner2)
    rect.setFill(strFillColor)
    rect.setOutline(strOutlineColor)
    rect.setWidth(2)
    rect.draw(win)
    return rect

def main():
    win = GraphWin("Draw Rectangles", 350, 350)
    win.setBackground("white")

    # Draw a message bar to display instructions and rectangle information.
    message = drawMessageBar(win)

    # Keep waiting for mouse clicks in a loop to draw multiple rectangles with
    # random colors.
    lstColors = [("royal blue", "dark blue"),
                 ("lime green", "dark green"),
                 ("tomato", "dark red"),
                 ("medium purple", "purple4"),
                 ("cornsilk", "tan"),
                 ("light steel blue", "steel blue"),
                 ("light salmon", "salmon4"),
                 ("turquoise", "turquoise4"),
                 ("chocolate", "chocolate4"),
                 ("gold", "gold4")]
    blnRun = True
    while blnRun:
        try:

            # Draw the next rectangle and display its area and perimeter.
            rect = drawUserRectangle(win, *random.choice(lstColors))
            message.setText("Area: {:,} pixels², Perimeter: {:,} pixels"
                            .format(*getRectInfo(rect)))

        except GraphicsError:
            blnRun = False

main()
