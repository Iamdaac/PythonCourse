import random

options = ["Rock", "Paper", "Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
    selection = random.randint(0,2)
    if selection == 1: 
        print(f"Computer choose {selection}, you lose!")
    else: 
        print(f"Computer choose {selection}, you win!")
elif user_input == 1:
    selection = random.randint(0,2)
    if selection == 2:
        print(f"Computer choose {selection}, you lose!")
    else: 
        print(f"Computer choose {selection}, you win!")
else: 
    selection = random.randint(0,2)
    if selection == 0:
        print(f"Computer choose {selection}, you lose!")
    else:
        print(f"Computer choose {selection}, you win!")