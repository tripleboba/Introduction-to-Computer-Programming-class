# Project:      Lab 5 (ChenTrinhLab05Sec03.py)
# Name:         Kuan-Yu Chen & Anh Trinh    
# Date:         02/01/16
# Description:  Calculating the average word length in a sentence


def AverageWordLength():

    #Greeting
    print("Welcome to the Average Word Length Calculator!")

    #Ask for the input
    strSentence = str(input("\nEnter Sentence: "))

    #Set the variables
    intCounterWords = 0
    letters = 0

    #Count the words in the sentence without 'space'
    intCounterWords += len(strSentence.split())

    #Count the all the characters in the sentence with space
    for characters in strSentence:

        #Count letters only (without spaces)
        letters += len(characters.split())
    
    #Calculate the average word length
    fltAverg = letters/intCounterWords

    #Display the output
    print("\nLetters in the sentence :", letters)
    print("The average words length:", fltAverg)

AverageWordLength()
