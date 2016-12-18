# Project:      Lab 4 (TrinhAsmareLab04Sec03.py)
# Name:         Anh Trinh & Samuel Asmare
# Date:         01/25/16
# Description:  Calculating BMI and telling their healthy range


def BMI():

    print("Welcome to the BMI Calculating Program!"
    "----------------------------------------")

    #Prompt the user for input
    intWeidth = int(input("Enter weight (in lbs):    "))
    intHeight = int(input("Enter height (in inches): "))
    print()

    #Calculate and print out the BMI
    intBMI = (intWeidth * 703)/(intHeight**2)
    print("BMI=",intBMI)

    #Set and display the healthy range
    if intBMI < 19:
        print("You are below the healthy range!")
    elif intBMI > 25:
        print("You are above the healthy range!")
    else:
        print("You are healthy!")

BMI()
