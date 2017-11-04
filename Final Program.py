# Project:      Final Program (TrinhAnhFinal.py)
# Name:         Anh Trinh
# Description:  This program will look through the master list(lstMaster)
#               for each "entry" (a person's name and 3 numbers).
#               You will add up all the numbers for each person and
#               send that total to a function that will return the square
#               root of that total.
#               You will then display the person's
#               name and the square root.
#
#               Example: Tim is associated with 20, 6 and 83. Adding up
#               the 20, 6 and 83 gives us 109 and the square root is
#               10.44030650891055.
#               The print out would be
#               Tim's square root is 10.44030650891055
#
#               You need to use a loop to add up the numbers. You should
#               end up having somewhere between 3-20 more
#               lines of code,no need for more.


import math

def sqrtFunction(intTotal):
    
    return math.sqrt(intTotal)


def main():

    # Create all 4 lists
    lstPerson       = ["Tim","Bob","Jon","Alf","Bea","Bear","Rabbit"]
    lstFirstNum     = [20,42,46,17,10,32,39]
    lstSecondNum    = [6,7,99,72,52,5,50]
    lstThirdNum     = [83,82,80,80,79,78,76]

    # Append the 4 lists to the Master List 
    lstMaster = []
    lstMaster.append(lstPerson)
    lstMaster.append(lstFirstNum)
    lstMaster.append(lstSecondNum)
    lstMaster.append(lstThirdNum)

    # code
    for i in range(len(lstMaster[0])):
        print(lstMaster[0][i] + "'s square root is " +
              str( sqrtFunction(lstMaster[1][i] + lstMaster[2][i] + lstMaster[3][i]) ))
     
main()
