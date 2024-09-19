# BMI Calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)  # The BMI formula
print(f"Your BMI is {bmi:.2f}")