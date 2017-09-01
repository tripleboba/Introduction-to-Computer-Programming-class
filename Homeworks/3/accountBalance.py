# Project:      Homework 3 (TrinhChenHW03Sec03.py)
# Name:         Anh Trinh & Kuan-Yu Chen
# Date:         02/10/16
# Description:  Program will compute a checking account balance

def accountBalance():
    
    try:
        
        #Greeting
        print("******** CHECKING ACCOUNT BALANCE ********\n")
        print("Total Available Balance: $0")

        #Set Variables
        fltBalance          = 0.0

        fltChargeAmount     = 0.0
        intChargeTimes      = 0
        
        fltDepositAmount    = 0.0
        intDepositTimes     = 0
        
        fltWithdrawalAmount = 0.0
        intWithdrawalTimes  = 0

        #Ask for input
        strAmount = str(input("\nEnter amount of money <type 'end' to exit>: $"))
        
        while strAmount != "end":

            #Convert string var to float var
            fltAmount = float(strAmount)
            
            if fltAmount < 0:
                print("Please enter valid $ amount")
            else:
                #Choose types of transaction
                print("---------------------- \nTo Deposit      <press 'd'> \nTo Withdraw     <press 'w'> \nService Charges <press 's'>")
                strService = str(input("Type of service: "))
                print("----------------------")
                
                #Deposit Service
                if strService        == "d":
                    intDepositTimes  += "d".count(strService)

                    fltDepositAmount += fltAmount
                    fltBalance       += fltAmount
                    print("Deposit Amount   : ${0:0.2f}".format(fltAmount))
                    print("Available Balance: ${0:0.2f}".format(fltBalance))

                #Withdraw Service
                elif strService         == "w":

                    if fltBalance < fltAmount:
                        
                        intChargeTimes  += 1
                        fltChargeAmount += 10
                        fltBalance      -= 10
                        print("\n*TRANSACTION DENIED: Insufficient funds for this transaction*")
                        print("\nService Charges          : $10")
                        print("Available Account Balance: ${0:0.2f}".format(fltBalance))

                    else:
                        intWithdrawalTimes  += "w".count(strService)
                        
                        fltWithdrawalAmount += fltAmount
                        fltBalance          -= fltAmount
                        print("Withdrawal Amount    : ${0:0.2f}".format(fltAmount))
                        print("Available Balance    : ${0:0.2f}".format(fltBalance))
                        
                #Check Service Charges
                elif strService    == "s":
                    intChargeTimes += "s".count(strService)

                    fltChargeAmount += fltAmount
                    fltBalance      -= fltAmount
                    print("Service Charge Amount: ${0:0.2f}".format(fltAmount))
                    print("Available Balance    : ${0:0.2f}".format(fltBalance))

                else:
                    print("Please enter available service! \n<d> Deposit \n<w> Withdraw \n<s> Service Charge")
                    
            print()
            strAmount = str(input("\nEnter amount of money <type 'end' to exit>: $"))

        #Display account balance, amount and numbers of deposits & withdrawals & service charges    
        print("\n*********** RECEIPT ***********")
        print("Number of Deposits:",intDepositTimes,"\nAmount of Deposits: ${0:0.2f}".format(fltDepositAmount))
        print("\nNumber of Withdrawals:",intWithdrawalTimes,"\nAmount of Withdrawals: ${0:0.2f}".format(fltWithdrawalAmount))
        print("\nNumber of Service Charges:",intChargeTimes,"\nAmount of Service Charges: ${0:0.2f}".format(fltChargeAmount))
        print("----------------------------- \nAccount Balance: ${0:0.2f}".format(fltBalance))
        print("\nThank You for using our service! \n~ Have A Good Day ~")
        
    except ValueError:
        print("Please enter number only! <'end' to exit> \n")
        accountBalance()
        
    except:
        print("Sorry! There is something wrong! Please contact us for helps!")

accountBalance()
