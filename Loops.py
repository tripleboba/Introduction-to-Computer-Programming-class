

def main():

    print("\t-------Character Loop-------")

    string = "We Can't Stop!"
    print("\nPrint string:'",string,"' vertically")
    for i in string:
        print(i)

    print("\nPrint in one line")
    for i in string:
        print(i,end="")

    print()

    print("\nSplit Words in a String (w/ spcaes)")
    for j in string:
        print(j.split())

    print("\t-------Numeric Loop-------")
    
    print("\nFrom 0 - 5...")
    for i in range(5):     
        print(i)        # from 0 - 5
        

    print("\n1st:0 - 5...  2nd:5 - 9...")
    for i in range(5):
        print("     ",i,"         ",i + 5)
        

    print("\nFrom 5 - 0...")
    for i in range(5):
        print(5 - i)   # from 5 - 0
        

    print("\nPrint string with loop...")
    for i in range(5):
        print("*" * i)

main()
