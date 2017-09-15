def main():

    # Set variable
    fltInput = 0.00

    # Ask for inputs 4 times
    for i in range (4):
        #Find the total
        fltInput += float(input("Enter number: "))

    # Display results
    print("\nTotal: ", fltInput,
          "\nAverage: ", fltInput / 4)

main()
