# This is a simple BMI (Body Mass Index) calculator
# BMI is calculated by dividing a person's weight in kilograms by the square of their height in meters

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Output the result
print("Your BMI is:", bmi)
# Please Like and Subscribe