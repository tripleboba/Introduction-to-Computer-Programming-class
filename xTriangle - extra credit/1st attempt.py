def xTriangle():

    intHeight = int(input("Enter triangle's height: "))

    print("\n-------- *Triangle --------")
    for intRow in range(intHeight):
        strX = 0
        while strX <= intRow:
            strX += 1
            print("X", end = "")
        print()

xTriangle()



    
