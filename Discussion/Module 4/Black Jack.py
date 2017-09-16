def blackJack():

    # Setup var
    cardSum = 0
    # List of possible cards
    cardNumber = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Prompt input 2 times
    for i in range(2):
        strCard = str(input("Card: ")).upper()

        if strCard == "A":
            cardSum += 11
        elif strCard == "J" or strCard == "Q" or strCard == "K":
            cardSum += 10
        elif int(strCard) in cardNumber:
            cardSum += int(strCard)
        else: print("Invalid Card")

    print("\nTotal number on both cards: "cardSum)

blackJack()
