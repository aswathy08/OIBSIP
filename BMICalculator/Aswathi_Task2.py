def bmi_calculator():
    try:
        # Input from user
        weight = float(input("Enter your weight (kg): "))
        height_cm = float(input("Enter your height (cm): "))

        # Convert cm to meters
        height_m = height_cm / 100  

        # BMI formula
        bmi = weight / (height ** 2)

        # Categorization
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Output
        print(f"Your BMI is {bmi:.2f}, Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the function
bmi_calculator()
