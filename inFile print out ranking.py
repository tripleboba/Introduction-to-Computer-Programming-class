def main():

    file = open("animal rank.txt", "r")
    lstRank = []
    
    for strLine in file:
        lstAnimal = strLine.split()
        lstAnimal[1] = int(lstAnimal[1])

        # If the list is empty or this breed has the lowest rank so far, add
        # this breed to the end.
        if len(lstRank) == 0 or lstAnimal[1] > lstRank[-1][1]:
            lstRank.append(lstAnimal)
        else:
            
            # Create a sorted list of breeds by comparing this breed's rank to
            # the other breeds in the list, and adding it in the right place.
            for i in range(len(lstRank)):
                if lstAnimal[1] < lstRank[i][1]:
                    lstRank.insert(i, lstAnimal)
                    break

    print("Highest ranking animal: {} (#{})\n".format(lstRank[0][0],
                                                     lstRank[0][1]))

    print("All animals (in order of ranking):")
    for lstAnimal in lstRank:
        print("#{}. {}".format(lstAnimal[1], lstAnimal[0]))

main()
