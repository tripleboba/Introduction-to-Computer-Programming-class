def main():

    # Prompt input
    intScore = int(input("Numeric score: "))

    if    intScore >= 90:  print("----\nGrade: A")
    elif  intScore >= 80:  print("----\nGrade: B")
    elif  intScore >= 70:  print("----\nGrade: C")
    elif  intScore >= 60:  print("----\nGrade: D")
    
    # 1st version
    # if 100 >= intScore >= 90:   print("----\nGrade: A")
    # elif 89 >= intScore >= 80:  print("----\nGrade: B")
    # elif 79 >= intScore >= 70:  print("----\nGrade: C")
    # elif 69 >= intScore >= 60:  print("----\nGrade: D")

main()
