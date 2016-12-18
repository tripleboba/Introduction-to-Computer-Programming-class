# Project:      Homework 1 (AnhTrinhHomework01Sec03.py)
# Name:         Anh Trinh
# Date:         01/15/16
# Description:  A program that allows 2 input numbers
#               and Display each number 6 times

def main():

    # Greeting
    print("Welcome To The Program!"
    "\n-----------------------")

    #Ask for user's inputs
    first = float(input("Enter the 1st number: "))
    second = float(input("Enter the 2nd number: "))

    print()

    #Display both numbers 6 times
    print("Displaying both numbers 6 times...")
    for i in range(6):
        print(first,second)

main()

