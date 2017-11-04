# Project:      Lab 8 (TrinhAnhLab08Sec03.py)
# Name:         Anh Trinh
# Date:         02/22/16
# Description:  A program will display a graphic of a 5 dice's side


from graphics import *

def dot(x,y,win):

    center = Point(x,y)

    circ = Circle(center,40)
    circ.setFill("black")

    return circ.draw(win)


##--------------------------------##

def dice(win):
    
    #Creating the white square
    dice = Rectangle(Point(100,100),Point(500,500))
    dice.setFill("white")

    #Displaying
    dice.draw(win)

    dot1 = dot(200,200,win)
    dot2 = dot(400,200,win)
    dot3 = dot(300,300,win)
    dot4 = dot(200,400,win)
    dot5 = dot(400,400,win)


##--------------------------------##

def main():
    
    win = GraphWin("Deep Cold",600,600)
    win.setBackground("Khaki")
    dice(win)
    
main()
