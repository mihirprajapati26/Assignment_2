# Ask the user for the length of the zander in centimeters
length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if length < 42:
    difference = 42 - length
    print(f"The zander is too small! It is {difference} centimeters below the size limit. Please release it back into the lake.")
else:
    print("The zander meets the size limit. You can keep it!")