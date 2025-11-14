"""
You have a sentence. Convert each word in the sentence
to uppercase and store it in list.

Expected Oupout:
['PYTHON', 'IS', 'FUN']
"""

text = "Python is fun"

upper = [word.upper() for word in text.split()]
print(upper)