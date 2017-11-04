from graphics import *


def visualSign(x,y,title,win):

    lblSign = Text(Point(x,y),title)
    lblSign.setTextColor("white")
    lblSign.setStyle("bold")
    lblSign.setSize(20)
    lblSign.draw(win)


##-------------------------------------------------------##

    
def visualText(x,y,title,size,win):

    txt = Text(Point(x,y),title)
    txt.setSize(size)
    txt.setTextColor("white")
    txt.draw(win)
    return txt


##-------------------------------------------------------##


def button(x,y,a,b,win):

    butt = Rectangle(Point(x,y),Point(a,b))
    butt.setFill("pink")
    butt.setOutline("white")
    butt.setWidth(2)
    butt.draw(win)

    
##-------------------------------------------------------##


def entryBox(x,y,win):

    box = Entry(Point(x,y),10)
    box.setFill("white")
    box.draw(win)
    return box


##-------------------------------------------------------##


def main():

    win = GraphWin("Add Up", 500,200)
    win.setBackground("light blue")

    #Visual Sign
    lblPlusSign = visualSign(140,80,"+",win)
    lblEqualSign = visualSign(300,80,"=",win)

    #Exit Button
    buttExit = button(458,170,498,198,win)
    buttExitTxt = visualText(478,184,"Exit",10,win)

    #Calulate Button
    buttCal = button(80,130,200,160,win)
    buttCalTxt = visualText(140,145,"Calculate...",12,win)

    #Output Displaying Spot
    lblOutput = visualText(400,80,"",30,win)

    #Entry Boxes
    boxEntry1 = entryBox(60,80,win)
    boxEntry2 = entryBox(220,80,win)

    blnRunning = True
    while blnRunning == True:

        clickXY = win.getMouse()
        intPointX = clickXY.getX()
        intPointY = clickXY.getY()
        
        #Clicking Calculate... Button
        if intPointX > 80 and intPointX < 200 and intPointY > 130 and intPointY < 160:
            intNum1 = int(boxEntry1.getText())
            intNum2 = int(boxEntry2.getText())
            intSum = intNum1 + intNum2

            #Displaying intSum
            lblOutput.setText(intSum)

        #Clicking Exit Button
        elif intPointX > 440 and intPointX < 498 and intPointY > 170 and intPointY < 198:
            blnRunning = False
            win.close()

main()
