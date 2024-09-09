# Start an infinite loop
while True:
    # Ask the user to enter a value in inches
    inches = float(input("Enter a value in inches (negative value to stop): "))
    
    # Check if the input is negative
    if inches < 0:
        print("Negative value entered. Exiting the program.")
        break
    
    # Convert inches to centimeters
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} centimeters.")