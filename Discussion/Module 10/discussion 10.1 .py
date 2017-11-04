def main():

    lstBooks = ["Da Vinci Code",
                "Rich Dad Poor Dad",
                "How to Wind Friends and Influence People",
                "20,000 Leagues Under the Sea",
                "Harry Potter"]

    lstPrices = [35, 9.4, 43.2, 0.99, 8.4]

    lstQuantities = [2, 5, 1, 4, 8]


    masterList = [lstBooks, lstPrices, lstQuantities]

    for i in range(5):
        print("The book",masterList[0][i],
              "has an inventory value of ${0:0.2f}".format(masterList[1][i]*masterList[2][i]),"\n")

main()
