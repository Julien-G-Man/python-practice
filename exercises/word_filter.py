"""
You have a list of strings.
Filter words that start with a vowel.

Expected output:
['apple']
"""

words = ['apple', 'banana', 'cherry', 'date']

for word in words:
    if word[0] == ('a' or 'e' or 'i' or 'o' or 'u'):
        print(word)
        
word = [word for word in words if word[0].lower() == ('a' or 'e' or 'i' or 'o' or 'u')]  
print(word)  

vowels = "aeiou"    
result = [word for word in words if word[0].lower() in vowels]
print(result)