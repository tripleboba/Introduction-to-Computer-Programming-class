from graphics import *

def setStairs(x,y,a,b,distance,win):
    
    for i in range(3):
        #startPoint(x,y)
        x += 40
        y -= 40

        #endPoint(a,b)
        a += 40
        b -= 40

        rec = Rectangle(Point(x,y),Point(a,b))
        rec.setFill("Salmon")
        rec.draw(win)

##------------------------------------##    

def setCircle(x,y,radius,win):

    #Setting a base circle
    circBase = Circle(Point(x,y),radius)
    circBase.setFill("Medium Slate Blue")

    #Second circle
    circTwo = Circle(Point(x + radius,y),radius)
    circTwo.setFill("Gold")

    #Displaying
    circBase.draw(win)
    circTwo.draw(win)

##------------------------------------##

def setBar(x,y,a,b,win):

    rec = Rectangle(Point(x,y),Point(a,b))
    rec.setFill("Green Yellow")

    txtTop = Text(Point(100,y - 10),"Top")
    txtTop.setTextColor("Green")

    txtBottom = Text(Point(100,b + 10),"Bottom")
    txtBottom.setTextColor("Green")

    #Displaying
    rec.draw(win)
    txtTop.draw(win)
    txtBottom.draw(win)
    
##------------------------------------##

def main():

    win = GraphWin("Shapes",400,400)

    #The base rectangle is (190,200),(270,240)
    #because of the loop, reduce x & a while increase y & b
    setStairs(150,240,230,280,40,win)
    
    setCircle(230,330,40,win)

    setBar(50,50,150,360,win)

main()



