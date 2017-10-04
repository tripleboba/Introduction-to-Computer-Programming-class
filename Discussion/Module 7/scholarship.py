def GPA(intClasses):
    print("\n**** GRADES ****\nA = 4.0\nB = 3.5\nC = 3.0\nD = 2.5\nF = 0.0\n****************")

    #Calculating grades and credits
    fltSumGrades = 0.0
    intSumCredits = 0

    #Grades
    for i in range(intClasses):
        print("\nClass",i+1)
        intCredits = int(input("Enter credits   : "))
        strGrades = str(input("Enter your grade: "))
        
        if strGrades == "A":
            fltSumGrades += 4.0 * intCredits
        elif strGrades == "B":
            fltSumGrades +=3.5 * intCredits
        elif strGrades == "C":
            fltSumGrades += 3.0 * intCredits
        elif strGrades == "D":
            fltSumGrades += 2.5 * intCredits
        elif strGrades == "F":
            fltSumGrades += 0.0 * intCredits
        else:
            print("Invalid Grades")

    #Credits
        intSumCredits += intCredits

    return fltSumGrades/intSumCredits


##--------------------------------------------##

def Eligible(fltGPA,intTotalCredits):

    intLetters = int(input("\nNumber of recommendation letters: "))
    if intLetters >= 2 and fltGPA >= 3.7 and intTotalCredits > 20:
        return ("\nEligible for scholarship")
    else:
        return ("\nNot eligible for scholarship")

##--------------------------------------------##
    
def scholarship():

    intClasses = int(input("Number of classes you've taken: "))
    intTotalCredits = int(input("\nTotal credits you've taken: "))

    fltGPA = GPA(intClasses)
    strEligible = Eligible(fltGPA,intTotalCredits)

    print(strEligible)

scholarship()
