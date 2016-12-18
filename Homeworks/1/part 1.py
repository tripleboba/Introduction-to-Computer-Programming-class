# Project:      Homework 1 (AnhTrinhHomework01Sec03.py)
# Name:         Anh Trinh
# Date:         01/15/16
# Description:  a program that calculates the MPH


def main():
    
    #Greeting
    print("Welcome to Calculating MPH Program"
    "\n----------------------------------\n")

    #Ask for inputs from user
    distance = float(input("Enter the riding distance ( in miles ): "))
    time = int(input("Enter the travel time ( in minutes )  : "))

    #Calculating the MPH
    mph = distance/(time/60)

    print()

    #Display the result
    print("Miles per Hour You Would Travel:", mph, "mph")

main()
