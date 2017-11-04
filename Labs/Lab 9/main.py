# Project:      Lab 9 (TrinhAnhLab09Sec03.py)
# Name:         Anh Trinh
# Date:         02/02/16
# Description:  The program shows off a students's scores imported
#               from a file. (bar chart form)


from graphics import *
import random

#Function creating a scale score
def scale(x,y,win):

    for i in range(0,110,10):

        # Between scores distance = 1 pixel
        x += 1
        
        scaleScore = Text(Point(x,y),i)
        scaleScore.setSize(10)
        scaleScore.setTextColor('Grey')
        scaleScore.draw(win)


##------------------------------------------------------##


#Function creating bars score
def bar(inFile,win):

    # Set Colors
    lstColors = ['light blue','turquoise','misty rose','green yellow',
                 'yellow green','tomato','gold','medium orchid',
                 'purple','black','tan','chocolate','pale violet red',
                 'light steel blue','salmon','orange','pale turquoise']

    # Width of bar scores is 1 pixel
    # Distance between bars score is 0.5
    barWidth = 1
    barDistance = 0.5
    # Set y coordinate
    y = 0

    # Get scores from the file
    for scores in inFile:
        lstScores = scores.split()
        # Set the scores to fit in the win.setCoords()
        intScores = (int(lstScores[0]))/10 + 1

        # Starting from the lowest bar's position (1,1)
        barScore = Rectangle(Point(1,1),Point(intScores, 1 + barWidth))
        
        # y coordinate for each new bar is old y += barWidth + barDistance
        y += barWidth + barDistance
        barScore = Rectangle(Point(1,y),Point(intScores, y + barWidth))

        barScore.setFill(random.choice(lstColors))
        barScore.setOutline('white')
        barScore.draw(win)

        # Displaying score text
        scoreTxt = Text(Point(intScores - 0.3, y + 0.5),int(lstScores[0]))
        scoreTxt.setTextColor('white')
        scoreTxt.setStyle('bold')
        scoreTxt.setSize(10)
        scoreTxt.draw(win)
        

##------------------------------------------------------##

        
def main():

    # Get user file input
    strFile = str(input("Enter file name: "))
    inFile = open(strFile + ".txt",'r')         # no need to type .txt at the end of the file's name

    # Creat win - set new coordinates
    win = GraphWin("Test Scores",500,400)
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    win.setBackground('white')

    # The title
    txtTitle = Text(Point(6,11),"5 Test Scores")
    txtTitle.setSize(20)
    txtTitle.setTextColor('dim gray')
    txtTitle.setStyle('bold')
    txtTitle.draw(win)

    # Displaying...
    # Scale start at Point(0,0.5)
    scaleScore = scale(0,0.5,win)
    bar(inFile,win)

main()
