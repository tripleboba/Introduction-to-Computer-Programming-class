# Project       :       Lab 07 (TrinhAnhLab07Sec03.py)
# Name          :       Anh Trinh
# Date          :       02/19/16
# Description   :       The program asks the user the pizza's diameter
#                       and price, then finds the cost/square inch

import math

# area function
def area(fltDiameter):
    return math.pi * ( ( fltDiameter/2 ) ** 2 )

# cost per square function
def cost(fltPrice, fltArea):
     return fltPrice / fltArea

# main function
def pizza():

    print("\t****** PIZZA IS LOVE ******\n"
          "********** PIZZA IS LIFE **********\n")

    # input from user
    fltDiameter = float(input("Diameter of the pizza: "))
    fltPrice    = float(input("Price of the pizza   : "))

    # output
    print("\nThe cost per square inch: ${0:0.3f}".format( cost( fltPrice, ( area(fltDiameter) ) ) ) )

pizza()
