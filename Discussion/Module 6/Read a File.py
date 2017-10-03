def ranking():

    #Open the dog.txt file
    inFile = open("dog.txt","r")

    intLargestNum = 9 #Lowest rank in the file: 9th
    strBreed = ""
    intRank = 0

    #Divide lines into dog breed and its rank
    #List of dog breeds: lstLines[0]
    #List of dog rank (convert to int type): int(lstLines[1])
    for lines in inFile:
        lstLines = lines.split() 

        if int(lstLines[1]) <= intLargestNum:
            intLargestNum = int(lstLines[1])

            #Set vars
            strBreed = str(lstLines[0])
            intRank   = intLargestNum

    #Output
    print("The Winner is:",strBreed,"-- Ranked:",intRank)
            
ranking()
