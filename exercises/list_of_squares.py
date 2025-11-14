"""
You have a list of numbers. Create a new list with the sqares of each number

Expected output:
[1, 4, 9, 16, 25]
"""

numbers = [1, 2, 3, 4, 5]

squares = [a**2 for a in numbers]
print(squares)