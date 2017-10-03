def fltSetDistance(sec):
    
    #Convert sound's speed from flt/sec to mile/sec
    speed = 1120/5280
    
    distance = sec * speed
    return distance


def lightningDistance():

    intSec = int(input("Time elapsed between the flash (in seconds): "))
    
    fltDistance = fltSetDistance(intSec)

    print("\nDistance to a lightning strike is:",round(fltDistance,2),"mile(s)")
    
lightningDistance()
