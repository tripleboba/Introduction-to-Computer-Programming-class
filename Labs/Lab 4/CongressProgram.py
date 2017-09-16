def congress():

    # Setup vars
    notStr            = "----\nNot eligible to run for Congress"
    senatorStr        = "----\nEligible to be a Senator"
    representativeStr = "----\nEligible to be a Representative"

    # Prompt input & check
    intAge = int(input("Age: "))
    if intAge < 25: print(notStr) # Under 25 condition

    else:
        fltYear = float(input("Year of citizenship: "))
        
        # Check conditions
        if fltYear >= 9:
            if intAge >= 30: print(senatorStr)
            else: print(representativeStr)
            
        elif fltYear >= 7:
            if intAge >= 25: print(representativeStr)

        else: print(notStr)

congress()
