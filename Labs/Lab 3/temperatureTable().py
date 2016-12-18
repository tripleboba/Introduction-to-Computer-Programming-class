def temperatureTable():

    #Greeting
    print("Equipvalent table of Celsius temperatures and the Fahrenheit every 10C degrees")
    print()

    print("Celsius Degree          Fahrenheit Degree")

    #Set Variables Value
    #the range start from 0, ends at 100, increment between numbers = 10
    for intCelsius in range(0,101,10):
        fltFahrenheit = 9/5 * intCelsius + 32 

        #Display Result
        print("    " , intCelsius , "                    " , fltFahrenheit)

temperatureTable()
