
            ## ------ CAPTURE ALL INPUTS INSIDE A LOOP ------ ##

def main():

    fltTotal = 0.0
    strAll = ""

    for i in range(3):
        fltNum = float(input("Enter a number: "))
        fltTotal += fltNum

    print()
    
    for i in range(3):
        strName = str(input("Enter a animal: "))
        strAll += ">" + strName + " "
        
    print("\nTotal  :",fltTotal,"\nAverage:",fltTotal/(i + 1))
    print("Animals:",strAll)

main()
