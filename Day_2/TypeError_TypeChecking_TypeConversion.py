# print(len("Hello"))

# Function that allows to know the data type
# print(type(True))
# print(type(3.14159))
# print(type(123456))
# print(type("This is str"))
# This is called type checked

# Type Conversion
# print(int("123") + int("456"))

# Code Challenge
# print("number of letters in your name: " + str(len(input("Enter your name: \n"))))

# Mathematical Operations
# Addition
# print(123 + 456)

# Substraction
# print(7 - 3)

# Multiplication
# print(6 * 6)

# Division
# print(4 / 2)

# Floor division    
# print(6 // 3)

# Exponentiation
# print(2**3)

# Modulus
# print(5 % 2)

# Code challenge 
# print(3 * 3 + 3 / 3 - 3) # = 7
# Change this code so it output 3 
# print(3 * (3 + 3) / 3 - 3)

# CODE CHALLENGE
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height ** 2

print(bmi)

# Number manipulation and F Strings

# Round the decimals
print(round(bmi))
finalBmi=(round(bmi, 2))


# Assigment Operator
score = 0
score += 1
print(score)

# f-strings
print(f"Your BMI score is {finalBmi} and your score is {score}")

# DAY 2 Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
if tip == 10:
    porcentaje_Bill = bill * 0.10
    almost_Bill = porcentaje_Bill + bill
elif tip == 12:
    porcentaje_Bill = bill * 0.12
    almost_Bill = porcentaje_Bill + bill
else: 
    porcentaje_Bill = bill * 0.15
    almost_Bill = porcentaje_Bill + bill
split = int(input("How many people to split the bill?\n $"))
totalBill = almost_Bill / split
print(f"Each person should pay: ${round(totalBill, 2)}" )
