
                    ## --------- Step Loop --------- ##

# Make equipvalent F degrees table for every 10C degrees

def temperatureTable():

    print("** Equipvalent table of Celsius temperatures \nand the Fahrenheit every 10C degrees ** \n")
    print("Celsius Degree        Fahrenheit Degree")

    for intCelsius in range (0,101,10):
        fltFahrenheit = 9/5 * intCelsius + 32
        print("     ",intCelsius,"                  ",fltFahrenheit)

temperatureTable()

# OR #

    for intCelsius in range(11):
        intCelsius = intCelsius * 10
        fltFahrenheit = 9/5 * intCelcius + 32
