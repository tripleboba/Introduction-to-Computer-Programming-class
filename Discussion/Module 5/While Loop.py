def main():

    # Setup var
    fltSum = 0.00

    # While loop stop when reach 100 ++
    while fltSum < 100:
        fltSum += float(input("Amount of $: "))

    print("----\nCongratulation, your $ input is > $100.\nTotal: $", fltSum)

main()
