"""
You have a list of numbers. Use a loop to print whether each number is even or odd.
"""

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")
     