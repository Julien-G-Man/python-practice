"""
Check is the string is a palindrome (reads the same forward and backwards)
"""

text = 'racecar'

is_palindrome = text == text[::-1]
print(is_palindrome)