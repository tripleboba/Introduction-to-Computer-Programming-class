
            ## ------- X TRIANGLE ------- ##

def xTriangle():

    intHeight = int(input("Enter triangle's height: "))

    print("\n-------- *Triangle --------")
    for intRow in range(intHeight):
        strX = 0
        while strX <= intRow:
            strX += 1
            print("*", end = "")
        print()
        
## OR ##

    print("\nx Triangle -- Print a blank line first")
    for i in range(intHeight + 1):
        print("X" * i)

xTriangle()



    
