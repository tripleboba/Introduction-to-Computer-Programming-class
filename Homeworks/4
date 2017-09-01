# Project:      HW4 (TrinhAnhHW04Sec03.py)
# Name:         Anh Trinh
# Date:         02/24/16
# Description:  The program will accept the user coffee type,
#               number of lbs, city and state, shipping method,
#               payment option inputs. Then calculating and
#               displaying user's choice of coffee type, lbs,
#               its cost, shippinf and handling cost, subtotal,
#               city and state, delivery method, payment type,
#               tax, and the total of the order.

def CoffeeCost(strCoffee):

    blnAvailable = True

    #Find the coffee type -> return its name & price
    while blnAvailable == True:

        if strCoffee == "JB":
            print("Jonestown Brew is your today choice! Yummy!")
            return 10.50, "Jonestown Brew"
        
        elif strCoffee == "PJ":
            print("Plymouth Jolt is your today choice! Tasty!")
            return 16.95, "Plymouth Jolt"          

        else:
            print("Oooopsie,",strCoffee,"is not offered today.")
            strCoffee = str(input("\nYour choice for today is: ")).upper()
            

##----------------------------------------##


def ShippingHandling(fltLbs):

    blnValid = True

    #Ask for Delivery Methods
    print ("\n---- DELIVERY METHODS ----    \n"
           "Overnight: $20.00               \n"
           "Two-Day  : $13.00               \n"
           "Standard : $0.00                \n"
           "--------------------------      \n"
           "Enter 'O' for Overnight option  \n"
           "      'T' for Two-Day   option  \n"
           "      'S' for Standard  option    ")
    strDelivery = str(input("\nDelivery Methods: ")).upper()

    #shipping($0.93/lb) + handling($2.50/order) costs var.
    fltShipHandlingFee = (0.93 * fltLbs) + 2.50

    while blnValid == True:

        if strDelivery == "O":
            print("***OVERNIGHT OPTION IS CHOSEN***")
            return 20.00, "Overnight", fltShipHandlingFee
        
        elif strDelivery == "T":
            print("***TWO-DAY OPTION IS CHOSEN***")
            return 13.00, "Two-day", fltShipHandlingFee
        
        elif strDelivery == "S":
            print("***STANDARD OPTION IS CHOSEN***")
            return 0.00, "Standard", fltShipHandlingFee
        
        else:
            print("!!Delivery Methods Unavailable!!")
            strDelivery = str(input("\nDelivery Methods: ")).upper()        
    
            
##----------------------------------------## 


def Tax(fltSubtotal):
    
    blnValid = True

    #Delivery Address: City and State
    print ("\n------ DELIVERY ADDRESS ------           \n"
           "(please enter abbreviation of a state)     \n"
           "(Ex: ship to Washington -> enter WA        \n"
           "------------------------------               ")
    strCity  = str(input("To  :(city)\t" )).upper()
    strState = str(input("    :(state)\t")).upper()
    
    while blnValid == True:
        strAddress = strCity + ", " + strState

        if len(strState) != 2:
            print("\n!!ERROR: Invalid State Input!!     \n"
                  "Please only abbreviation of a state  \n")
            strCity  = str(input("To  :(city)\t" )).upper()
            strState = str(input("    :(state)\t")).upper()

        elif strState == "WA" or strState == "CA" or strState == "TX":
            return 0.09 * fltSubtotal,strAddress
        
        elif strState == "OR" or strState == "FL":
            return 0.0 * fltSubtotal,strAddress
        
        else:
            return 0.07 * fltSubtotal,strAddress


##----------------------------------------##


def Payment(fltSubtotal):

    blnValid = True
        
    print("\n---- PAYMENT METHODS ----      \n"
          "Using Paypal     : <enter 'P'>   \n"
          "      Check      : <enter 'C'>   \n"
          "      Credit Card: <enter 'CC'>  \n"
          "--------------------------          ")
    strPayment = str(input("\nPayment Method: ")).upper()

    while blnValid == True:
        
        if strPayment == "P":
            #3% increase on subtotal
            print("***PAYPAL METHOD IS CHOSEN: +3% fee on subtotal***")
            return "Paypal", (0.03 * fltSubtotal)
                    
        elif strPayment == "C":
            #2% discount on subtotal
            print("***CHECK METHOD IS CHOSEN: discount 2% fee on subtotal***")
            return "Check", (-0.02 * fltSubtotal)
        
        elif strPayment == "CC":
            #5% increase on subtotal
            print("****CREDIT CARD METHOD IS CHOSEN: +5% fee on subtotal***")
            return "Credit Card", (0.05 * fltSubtotal)
        
        else:
            print("!!Payment Method Unavailable!!")
            strPayment = str(input("\nPayment Method: ")).upper()


##----------------------------------------##

        
def TheKonditoreiCoffeeShop():
    try:

        #Greeting
        print("\n\t\t____WELCOME TO THE KONDITOREI COFFEE SHOP____\n")

        print("\n---- TODAY OFFERS ----       \n"
              "Jonestown Brew: $10.50 / lb    \n"
              "Plymouth Jolt : $16.95 / lb    \n"
              "----------------------         \n"
              "Enter 'JB' for Jonestown Brew  \n"
              "      'PJ' for Plymouth Jolt     ")

        #Ask for type of coffee & find the cost
        strCoffee = str(input("\nYour choice for today is: ")).upper()

        #Coffee cost per lb & Type
        fltCoffeePriceLb, strCoffee = CoffeeCost(strCoffee)
        
        #Ask for the amount
        try:
            fltLbs = float(input("\nHow many Lbs you need?: "))
        except ValueError:
            print("Please enter numeric input...")
            TheKonditoreiCoffeeShop()

        #Coffee cost
        fltCoffeeCost = fltCoffeePriceLb * fltLbs

        #Delivery chosen option fee, service name, fltShipHandlingFee
        fltDeliOptFee, strDeliOpt, fltShipHandlingFee = ShippingHandling(fltLbs)

        #Subtotal
        fltSubtotal = fltCoffeeCost + fltShipHandlingFee

        #Tax Cost and City & State
        fltTax, strAddress = Tax(fltSubtotal)

        #Payment chosen option & fee
        strPayOpt, fltPayOptFee = Payment(fltSubtotal)
        
        #Total
        fltTotal = fltSubtotal + fltDeliOptFee + fltTax + fltPayOptFee

        #Displaying....
        print("\n\t******* ORDER ******* \n"
              "Coffee Type              :\t",strCoffee,"\n"
              "Amount                   :\t",fltLbs,"lb(s)\n"
              "Price                    :\t ${0:0.2f}".format(fltCoffeeCost),"\n"
              "Shipping & Handling Fee  :\t ${0:0.2f}".format(fltShipHandlingFee),"\n"
              "Subtotal                 :\t ${0:0.2f}".format(fltSubtotal),"\n\n"
              
              "Destination              :\t",strAddress,"\n"
              "Tax                      :\t ${0:0.2f}".format(fltTax),"\n"
              "Delivery Method          :\t",strDeliOpt,"\n"
              "Delivery Method Fee      :\t ${0:0.2f}".format(fltDeliOptFee),"\n\n"

              "Payment Method           :\t",strPayOpt,"\n"
              "Payment Method Fee       :\t ${0:0.2f}".format(fltPayOptFee),"\n"
              "----------------------------------- \n"
              "Total:\t ${0:0.2f}".format(fltTotal))
    except:
        print("So Sorry! The program crashes. Please contact us for helps.")

TheKonditoreiCoffeeShop()
