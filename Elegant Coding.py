def main():

        ##-------- ASSIGN LONG DISPLAY OUTPUT --------##
    
    userInput = str(input("Enter a animal: "))
    animal = userInput.lower()

    Cat    = "Meow Meow"
    Dog    = "Woof Woof"
    Fish   = "Bluh Bluh"
    Nah    = "Sorry. We haven't upload that animal's data"
    
    if animal == "cat":
        print(Cat)
    elif animal == "dog":
        print(Dog)
    elif animal == "fish":
        print(Fish)
    else:
        print(Nah)

    print("\n------------------------------------\n")
    
        ##-------- EASY TO READ LONG STRING --------##

    print("A string long like this\n"
          "should be written like this \n"
          "since it's easy to read! It"
          "\ncould be used for asking input")

main()
