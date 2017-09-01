# fixing the problem in 2nd attempt - extra blank line at 1st

def xTriangle():

    intHeight = int(input("Enter triangle's height: "))
    
    for i in range(intHeight):
        print( "X" * (i+1) )    # start @ 0 -> +1 to start printing 1st X

xTriangle()



    
