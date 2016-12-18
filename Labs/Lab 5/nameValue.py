# Project:      Lab 5 (ChenTrinhLab05Sec03.py)
# Name:         Kuan-Yu Chen & Anh Trinh    
# Date:         02/01/16
# Description:  Taking user string input
#               and summing up the values of the letters of the string


def NameValue():

    #Greeting
    print("Welcome to the Numeric Value Name Calculator!")

    #Ask for the input
    strName = str(input("\nEnter your name: "))

    #Change the uppercase letters in the string to lowercase letters
    strNameL = strName.lower()

    #Set the variable intNameValue
    intNameValue = 0

    #Since ord('a') = 97 then to make 'a' = 1 -> ord() - 96
    for ch in strNameL:
        intNameValue += ord(ch)-96

    #Displpay result
    print("\nName:",strName)
    print("Your name numeric value =",intNameValue)

NameValue()
