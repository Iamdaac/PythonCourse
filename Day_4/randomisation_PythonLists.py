# random.randint(a,b) create a random integer
import random

# randomNumber = random.randint(1, 10)
# print(randomNumber)

# import myModule - We can call other information like this
# print(myModule.my_favorite_number) - When we call for the info in "myModule" also call for the variable name

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10) 
# print(random_float)

random_head_tails = random.randint(0,1)
if random_head_tails == 0:
    print("Heads!")
else:
    print("Tails!")