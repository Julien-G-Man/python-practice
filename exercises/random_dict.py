"""
Given a list of names and programs. Assign a random program to each person in a dictionary
without repetition and ensure that no two people have the same program
"""

import random

diction = {}
names = ['Julien', 'Aman', 'Frank', 'Sam']
programs = ['computer science', 'engineering', 'medecine', 'law', 'business admin']

for name in names:
    program = random.choice(programs)
    diction[name] = program    
    programs.remove(program)
    
print(diction)    