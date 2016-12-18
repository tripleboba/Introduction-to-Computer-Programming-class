# Project:      Lab 03 (TrinhAnhLab03Sec03.py)
# Name:         Anh Trinh
# Date:         01/20/2016
# Description:  Program will compute and prints a table of
#               C and F temperatures every 10 degrees from 0C - 100C


def temperatureTable():

    #Greeting
    print("Equipvalent table of Celsius temperatures and the Fahrenheit every 10C degrees\n")

    print("Celsius Degree          Fahrenheit Degree")

    #Set Variables Value
    #range starts from 0, ends at 100, increment between numbers = 10
    for intCelsius in range(0,101,10):
        fltFahrenheit = 9/5 * intCelsius + 32 

        #Display Result
        print("    " , intCelsius , "                    " , fltFahrenheit)

temperatureTable()
