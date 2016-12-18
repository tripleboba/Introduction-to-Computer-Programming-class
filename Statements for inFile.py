
            ## ------ STATEMENTS FOR INFILE ------ ##
def main():
    inFile = open("min-max rank.txt",'r')
    print("Ranking based on numeric and alphabet orders")
    print(min(inFile))
    #Since the whole file is read @ this state, can't process anymore
main()

def mainB():
    inFile = open("min-max rank.txt",'r')
    for items in inFile:
        lstItems = items.split()

mainB()
