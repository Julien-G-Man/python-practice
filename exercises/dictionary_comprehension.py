"""
You have a list of fruits and their prices.
Create a dictionary where keys are fruits and values are prices multiplied by 1.1 (adding 10% tax)
"""

fruits = ['apple', 'banana', 'cherry']   
prices = [100, 200, 300]

fruit_prices = {fruits[i]: (prices[i] * 1.1) for i in range(len(fruits))}