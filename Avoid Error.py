
            ## ------ AVOID ERROR ------ ##

def main():

    try:        # put code here
        
        print("displaying...")
        abc
        
    except:     # put notification

        print("\nThe program blew up! Sorry!")

main()

def mainA():

    try:
        intNum = int(input("\nEnter integer: "))
        fltNum = float(input("Enter decimal: "))

        print("Int num:",intNum,"\nDecimal:",fltNum)

    except ValueError:                  # input wrong type

        print("Enter integer only!")    # intNum = 0.9

    except:                             # for other error

        # if not about ValueError -> jump to this part
        print("\nThe program blew up! Sorry!")

mainA()
