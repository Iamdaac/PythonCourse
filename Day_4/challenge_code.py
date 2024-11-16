import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends)) first option with .choice(a)

who_pay = random.randint(0,4)
# print(friends[who_pay]) second option 

if who_pay == 0:
    print(friends[0])
elif who_pay == 1:
    print(friends[1])
elif who_pay == 2:
    print(friends[2])
elif who_pay == 3: 
    print(friends[3])
else: 
    print(friends[4])

