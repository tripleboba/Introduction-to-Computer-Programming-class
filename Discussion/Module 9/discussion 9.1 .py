from graphics import *

def getArea(length,width,win):

    area = length * width
    
    textArea = Text(Point(0.7,1),"Area:")
    textArea.setSize(10)
    textArea.draw(win)

    AreaLbl = Text(Point(2.5,1),round(area,2))
    AreaLbl.setSize(10)
    AreaLbl.draw(win)
    

##------------------------------##

def getPerimeter(length,width,win):
    
    perimeter = 2*(length + width)

    textPeri = Text(Point(1.1,0.5),"Perimeter:")
    textPeri.setSize(10)
    textPeri.draw(win)

    PeriLbl = Text(Point(2.5,0.5),round(perimeter,2))
    PeriLbl.setSize(10)
    PeriLbl.draw(win)

##------------------------------##

def main():

    win = GraphWin("Rectangle",400,300)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("light blue")

    #Get clicks from the user
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    #find the coordinates of 2 points
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    
    #check if 2 point would make a square
    if x1 == y1 and x2 == y2:
        lblTxt = Text(Point(0.2,0.2),"Your 2 point will draw a square.\nPlease click again")
        lblTxt.setSize(10)
        lblTxt.setStyle("bold")
        lblTxt.setTextColor("Salmon")
        lblTxt.draw(win)
        main()

    #draw the rectangle
    else:
        rec = Rectangle(p1,p2)
        rec.setFill("pink")
        rec.setOutline("white")
        rec.setWidth(3)
        rec.draw(win)

        #Find the length & width of the rec.
        length = abs(x1-x2)
        width = abs(y1-y2)

        #displaying the area & perimeter
        displayBox = Rectangle(Point(0,0),Point(3.5,1.5))
        displayBox.setFill("white")
        displayBox.setOutline("white")
        displayBox.draw(win)

        recArea = getArea(length,width,win)
        recPeri = getPerimeter(length,width,win)

main()
