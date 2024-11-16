# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi <= 25:
#     print("normal weight")
# else: 
#     print("overweight")

# Project: Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? \n Type 'left' or 'right'\n").lower()
if direction == 'left':
    optionLake = input("You've come to a lake. There is an island in the middle of the lake. \n Type 'wait' to wait for the boat. Type 'swin' to swin across.\n").lower()
    if optionLake == 'wait':
        colorDoor = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n").lower()
        if colorDoor == 'yellow':
            print("You win!")
else:
    print("Game Over.")

