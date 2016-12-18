# Project:      Lab 6 (TrinhAnhLab06Sec03.py)
# Name:         Anh Trinh
# Date:         02/08/16
# Description:  The program counts the number of lines, words,
#               and characters in an imported file

def wordCount():

    #Ask for impoted file's name
    strFileName = str(input("Enter the file name: "))

    #Open the imported file
    inFile = open(strFileName,"r")

    #Set Variables
    intWords      = 0
    intCharacters = 0
    strData = inFile.read()               # 1

    #Count the lines in the file
    intLines = len(inFile.readlines())    # 2

    #Count the words in the file (don't count spaces)
    intWords += len(strData.split())

    #Count the characters in the file
    for characters in strData:             # 3
        intCharacters += len(characters.split())

    #Display the output
    print("Data in file:",strFileName,"\n------------------")
    print(strData)
    print("------------------\nNumber of words     :",intWords,"\nNumber of lines     :",intLines,"\nNumber of characters:",intCharacters)
    
wordCount()

              # INSTRUCTOR's COMMENT #
# reading the object inFile 3 times: should only do it once
