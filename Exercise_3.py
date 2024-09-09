# Ask for the biological gender and hemoglobin value
gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin = int(input("Enter your hemoglobin value (g/l): "))

# Check the hemoglobin value based on gender
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender entered.")