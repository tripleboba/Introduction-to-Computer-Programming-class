# Project:      Lab 03 (TrinhAnhLab03Sec03.py)
# Name:         Anh Trinh
# Date:         01/20/2016
# Description:  Program1 will calculate the cost of a coffee
#               shop's products
#               Program2 will compute and prints a table of
#               C and F temperatures every 10 degrees from 0C - 100C

def coffeeShop():

    #Greeting
    print("Welcome to the Konditorei Coffee Shop!\n")

    #User's Input
    fltPound = float(input("Enter the amount of coffee (in pounds): "))
    print()
    
    #Set Variables Value
    fltPrice = 10.50 * fltPound         #$10.50 per pound
    fltShippingFee = 0.86 * fltPound    #$0.86 per pound
    fltOverhead = 1.50                  #fixed cost
    
    fltTotal = fltPrice + fltOverhead + fltShippingFee

    #Display The Result - round up to 2nd decimal place
    print("Amount      :  " , fltPound , "lb(s)")
    print("Price       : $" , round(fltPrice,2) )
    print("Shipping fee: $" , round(fltShippingFee,2) )
    print("Overhead fee: $" , fltOverhead)
    print("--------------------------")
    print("Total:        $" , round(fltTotal,2) )

coffeeShop()
