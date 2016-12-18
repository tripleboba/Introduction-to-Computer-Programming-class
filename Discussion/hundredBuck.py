# Create a program that uses a while loop that asks the user to
# input $ amounts over and over until the the accumulated amount 
# exceeds $100. At that point give a congratulatory message. 


def hundredBuck():

    #Assign values for total $ amount input and fixed $ to win
    fltTotal = 0.0
    fltWin = 100.0
    
    while fltTotal < fltWin:
        fltAmount = float(input("Enter $ amounts: "))
        fltTotal += fltAmount

        if fltAmount <= 0:
            print("\nPlease enter valid $ value")

        #Exit and Display when the input amount >= $100
        if fltTotal >= fltWin:
            print("\nCongratulatory!")

hundredBuck()
