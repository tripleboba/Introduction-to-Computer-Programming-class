
            ## ------ STATEMENTS FOR STRING ------ ##
def main():

    print("Numeric Value of A Character")
    print("'a':",ord("a"),"\n'b':",ord("b"))

    print("\nString Value of A Number")
    print("'97':",chr(97),"\n'98':",chr(98))
    

    print("\nNumeric Length of A String")
    string = "How are you"
    
    print("'",string,"' (w/ space) :",len(string),"letters")
    print("'",string,"' (w/o space):",len(string.split()),"letters")
    
    count = 0
    for i in string:
        count += len(i.split())
    print("'",string,"' (w/o space):",count,"words")

    print("\nSeperate a String (seperating words w/o spaces)")
    string = "Baba Black Sheep"
    print("Baba Black Sheep:",string.split())

    


main()
