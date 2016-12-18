# Project:      Homework 2 (TrinhAsmareHomework02Sec03.py)
# Name:         Anh Trinh & Samuel Asmare
# Date:         01/29/16
# Description:  The program takes user input for 3 items
#               and calculates the order's cost

def shop():
    
    #Greeting
    print("           WELCOME TO THE SHOP!         \n"
    "----------------------------------------");

    #Set the varibles: Subtotal, Total order's weight, Products
    fltSubtotal = 0.0
    fltLbsTotal = 0.0
    strProducts = ""
    
    #Prompt user for input
    for i in range(3):
        strProduct  = str(input("\nEnter product's name          : "))
        intQuantity = int(input("      the quantity            : "))
        fltPrice    = float(input("      price for this product  :$"))
        fltLbs      = float(input("      weight per item (in lbs): "))

        #Calculate the Subtotal, Total order's weight, & Products
        strProducts += "+" + strProduct + "  "
        fltLbsTotal += fltLbs   * intQuantity
        fltSubtotal += fltPrice * intQuantity

    #Calculate the Shipping and Handling fee, Tax, Total
    #Tax = 8.5%, fixed charge $5/order, 25 cents/lb
    fltShipHandle = (0.25 * fltLbsTotal) + 5.00
    fltTax        = (fltSubtotal + fltShipHandle) * 0.085
    fltTotal      = fltSubtotal + fltShipHandle + fltTax
    
    #Display the output
    #Format the float variables to round to the 2nd decimal place
    print("\n|||||||||||||||| CHECKOUT ||||||||||||||||\n")
    print("Products    :",strProducts)
    print("Subtotal    : ${0:0.2f}".format(fltSubtotal))
    print("Tax         : ${0:0.2f}".format(fltTax))
    print("Shipping fee: ${0:0.2f}".format(fltShipHandle))
    print("_________________________\nTotal       : ${0:0.2f}".format(fltTotal))
    
shop()

                             ## --- TEST DATA --- ##
#   Shovel : $25.00 1 each 6 lbs
#   Planter: $45.00 2 each 11 lbs
#   Broom  : $12.00 1 each 4 lbs
# Subtotal = $127.00, Tax = $11.90, Shipping = $13.00, Total = $151.90
