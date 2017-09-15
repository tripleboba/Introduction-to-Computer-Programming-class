def main():
  
    # Capture 4 inputs
    intInput = 4
  
    # Set var
    fltSum = 0.00
  
    # Ask for input 4 times
    for i in range (intInput):
        fltNumber =  float(input("Enter number: "))
    
        # Calculate the total
        fltSum = fltSum + fltNumber
     
    # Caculate the average
    fltAvg = fltSum / intInput
  
    # Display the result
    print("\nTotal: ", fltSum)
    print("Average: ", fltAvg)
  
main()
