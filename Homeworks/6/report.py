# Project:      Homework 6 (TrinhAnhHW6Sec03.py)
# Name:         Anh Trinh
# Date:         03/21/16
# Description:  The program will import an input info file
#               & display info stored in the file. Then, wait
#               for the user's choice of report.


from graphics import *


def button(win):

    # Report Buttons
    cDistance = 0
    
    for i in range(4):
        reportButt = Circle(Point(10,90),20)
        reportButt.move(50,cDistance)

        reportTxt = Text(Point(0,90),i+1)
        reportTxt.move(60,cDistance)
        
        cDistance += 60
        
        reportButt.setFill("Light Steel Blue")
        reportButt.setOutline("white")
        reportButt.setWidth(4)
        reportTxt.setStyle("bold")

        reportButt.draw(win)
        reportTxt.draw(win)


##-----------------------------------------##


def design(win,entryBox):
    
    # Background
    win.setBackground("Lavender")

    # Entry Box
    entryBox.setFill("white")
    entryBox.setText("file's name...")
    entryBox.setStyle("italic")

    # Pink Part
    pinkPart = Rectangle(Point(0,350),Point(600,400))
    pinkPart.setFill("Misty Rose")
    pinkPart.setOutline("Misty Rose")
    pinkPart.draw(win)


##-----------------------------------------##


def report1and4Display(win,report,reportOutFileName):
    
    msgDisplaySpot = Rectangle(Point(150,10),Point(590,340))
    msgDisplaySpot.setFill("Lavender")
    msgDisplaySpot.setOutline("Lavender")
    msgDisplaySpot.draw(win)

    lblReport = Text(Point(370,150),report)
    lblReport.setSize(15)
    lblReport.setStyle("bold")
    lblReport.draw(win)

    lblMsg = Text(Point(370,200),"Data has been written to file: " + reportOutFileName)
    lblMsg.setStyle("italic")
    lblMsg.draw(win)

    
##-----------------------------------------##


def report2and3Display(win,report,mListData):

    # Report 2 & 3 Display
    msgDisplaySpot = Rectangle(Point(150,10),Point(590,340))
    msgDisplaySpot.setFill("Lavender")
    msgDisplaySpot.setOutline("Lavender")
    msgDisplaySpot.draw(win)

    lblReport = Text(Point(370,50),report)
    lblReport.setSize(15)
    lblReport.setStyle("bold")
    lblReport.draw(win)

    # Report 3 Additional Display
    if report == "Report 3":
        percentFBPL = report3(mListData)
        
        lblPercent = Text(Point(370,150),str(percentFBPL) + "%")
        lblPercent.setSize(20)
        lblPercent.setStyle("bold")
        lblPercent.draw(win)
        Text(Point(370,200),"of families that fall below the poverty level").draw(win)


##-----------------------------------------##


def importFile(win,entryBox):

    lstID     = []
    lstMember = []
    lstIncome = []
    lstState  = []
     
    # Import and Open Input File
    strFileName = str(entryBox.getText())
    inFile = open(strFileName,"r")
    
    for data in inFile:
        lstData = data.split()
        
        # Convert str list to int list
        intLstMember = int(lstData[1])
        intLstIncome = int(lstData[2])

        # Lists
        lstID.append(lstData[0])
        lstMember.append(intLstMember)
        lstIncome.append(intLstIncome)
        lstState.append(lstData[3])

    inFile.close()

    # masterList
    mListData = [ lstMember, lstIncome, lstState, lstID ]

    return mListData


##-----------------------------------------##


def report1(mListData):

    report1File = open("Trinh_Anh_report01.txt",'w')

    belowPL = []
    
    #----------- Income Check for AK State -----------
    for i in (i for i,strState in enumerate(mListData[2]) if strState == "AK"):

        intMember = mListData[0][i]
        intIncome = mListData[1][i]

        # Additional member: + $3,980
        incomePLCheck = (intIncome - (3980 * (intMember - 1) ))

        # Poverty Level Income of 1 person in AK = $11,630
        if incomePLCheck < 11630:
            
            strFamilyBelowPL = ( mListData[3][i]        + " " +
                                 str(mListData[0][i])   + " " +
                                 str(mListData[1][i])   + " " +
                                 mListData[2][i]                 )
            
            print(strFamilyBelowPL, file = report1File)
            
            belowPL.append(strFamilyBelowPL)

    
    #----------- Income Check for HI State -----------
    for i in (i for i,strState in enumerate(mListData[2]) if strState == "HI"):

        intMember = mListData[0][i]
        intIncome = mListData[1][i]

        # Additional member: + $3,660
        incomePLCheck = (intIncome - (3660 * (intMember - 1) ))

        # Poverty Level Income of 1 person in AK = $10,700
        if incomePLCheck < 10700:
            
            strFamilyBelowPL = ( mListData[3][i]        + " " +
                                 str(mListData[0][i])   + " " +
                                 str(mListData[1][i])   + " " +
                                 mListData[2][i]                 )
            
            print(strFamilyBelowPL, file = report1File)
            
            belowPL.append(strFamilyBelowPL)
            

    #----------- Other States -----------
    for i in (i for i,strState in enumerate(mListData[2]) if strState != "AK" and strState != "HI"):
  
        intMember = mListData[0][i]
        intIncome = mListData[1][i]

        # Additional member: + $3,180
        incomePLCheck = (intIncome - (3180 * (intMember - 1) ))

        # Poverty Level Income of 1 person in AK = $10,700
        if incomePLCheck < 9310:
            strFamilyBelowPL = ( mListData[3][i]        + " " +
                                 str(mListData[0][i])   + " " +
                                 str(mListData[1][i])   + " " +
                                 mListData[2][i]                 )

            print(strFamilyBelowPL, file = report1File)

            belowPL.append(strFamilyBelowPL)
            
    report1File.close()

    # Add belowPL list to use for Report 3
    return belowPL


##-----------------------------------------##

def report2(win,mListData):
    
    # Find the average income
    b = 0
    avgIncome = 0
    lstFamilyAboveAvgIncome = []

    for incomes in mListData[1]:
        avgIncome += round( incomes / len(mListData[1]), 1)
    
    # Add incomes > avgIncome to a lsit
    for i in (i for i, intIncome in enumerate(mListData[1]) if intIncome > avgIncome):
        
        strFamilyAboveAvgIncome = ( mListData[3][i]       + " " +
                                    str(mListData[0][i])  + " " +
                                    str(mListData[1][i])  + " " +
                                    mListData[2][i]                 )
    # Display
        Text(Point(370,80),"(average income: $" + str(avgIncome) + ")").draw(win)
        b += 30
        Text(Point(370,b + 100),strFamilyAboveAvgIncome).draw(win)
        

##-----------------------------------------##


def report3(mListData):
    
    lstFamiliesBelowPL = report1(mListData)
    percentFamiliesBelowPL = round( 100 * (len(lstFamiliesBelowPL) / len(mListData[3])) , 1)

    return percentFamiliesBelowPL


##-----------------------------------------##


def report4(mListData):

    belowPL = report1(mListData)
    

    report4File = open("Trinh_Anh_report04.txt",'w')

    for i in range(len(mListData[3])):
        setData = ( str(mListData[3][i]) + " " +
                    str(mListData[0][i]) + " " +
                    str(mListData[1][i]) + " " +
                    str(mListData[2][i])         )

        if setData in belowPL:
            setData += "\t\t [below]"

        print(setData, file = report4File)

    report4File.close()


##-----------------------------------------##

    
def main():

    try:
        
        win = GraphWin("Report",600,400)
        # Get File Input
        entryBox = Entry(Point(110,375),20)
        entryBox.draw(win)

        # Design
        visual = design(win,entryBox)

        # Import and Close Button    
        rDistance = 0

        for i in range(2):
            butt = Rectangle(Point(220,365),Point(290,385))
            butt.move(rDistance, 0)
            
            rDistance += 300

            butt.setFill("white")
            butt.setOutline("white")
          
            butt.draw(win)

        Text(Point(255,375),"import").draw(win)
        Text(Point(555,375),"close").draw(win)


        blnRun = True

        while blnRun == True:
            getClick = win.getMouse()
            xClick = getClick.getX()
            yClick = getClick.getY()

            # importing...
            if xClick > 220 and xClick < 290 and yClick > 365 and yClick < 385:
                mListData = importFile(win,entryBox)
                buttons = button(win)
                
            # Report 1
            elif xClick > 30 and xClick < 80 and yClick > 60 and yClick < 110:
                 report1(mListData)
                 report1and4Display(win,"Report 1","Trinh_Anh_report01.txt")
                
            # Report 2
            elif xClick > 30 and xClick < 80 and yClick > 130 and yClick < 170:
                report2and3Display(win,"Report 2",mListData)
                report2(win,mListData)

            # Report 3
            elif xClick > 30 and xClick < 80 and yClick > 200 and yClick < 230:
                report3(mListData)
                report2and3Display(win,"Report 3",mListData)

            # Report 4
            elif xClick > 30 and xClick < 80 and yClick > 260 and yClick < 280:
                report4(mListData)
                report1and4Display(win,"Report 4","Trinh_Anh_report04.txt")
                
            #closing...
            elif xClick > 530 and xClick < 590 and yClick > 365 and yClick < 385:
                blnRun = False
                win.close()
                

    except FileNotFoundError:
        win.close()
        
        winR = GraphWin("FileNotFoundError",400,100)
        txtTitle = Text(Point(100,20),"File Not Found Error")
        txtTitle.setTextColor("red")
        txtTitle.setStyle("bold")
        txtTitle.draw(winR)

        txtBody = Text(Point(200,70),"Please enter a file to import \n"
                                                     "or \n"
                                     "Check again the file's name/location")
        txtBody.setTextColor("red")
        txtBody.setSize(10)
        txtBody.setStyle("italic")
        txtBody.draw(winR)
        
        main()
        

main()
