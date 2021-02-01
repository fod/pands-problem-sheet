# bmi.py
# A program that calculates BMI from weight and height values entered by the user
# Author: Fiachra O' Donoghue

print("BMI Calculator")
print("--- ----------")

# Request user input their weight in kilos and height in centimetres 
# and assign the results to the 'weight' and 'height' variables respectively
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in centimetres: "))

# Convert height to metres
height /= 100

# Calculate BMI using the formula weight(kg) / height(m)^2
bmi = weight / (height ** 2)

# Output BMI formatted to 2 decimal places
# [ref] https://docs.python.org/3/library/string.html#format-specification-mini-language
print("Your BMI is {:.2f}".format(bmi))

