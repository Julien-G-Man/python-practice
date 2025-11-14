"""
Create a list of 10 random numbers, then pick a random number from the created a list
"""

import random
random_list = []

for i in range(20):
    random_list.append(random.randint(1, 100))
    
print(random_list)    

number = random.choice(random_list)
print(f"{number} at index {random_list.index(number)}")