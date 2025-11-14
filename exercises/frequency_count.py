"""
Given the following string (text), count the frequency of each chaeacter
(excluding spaces)

Expected output:
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

text = "hello world"

texts = text.replace(" ", "")
print(texts)
char_list = []
freq_list = []
p = 0

for char in texts:
    freq = text.count(char)
    char_list.insert(p, char)
    freq_list.insert(p, freq)
    p += 1

diction = {}
for char, freq in zip(char_list, freq_list):
    if char == " ":
        char = None 
        diction[char] = None
    diction[char] = freq
print(diction)    

# simple solution with Counter library
from collections import Counter

char_count = Counter(text.replace(" ", ""))
print(dict(char_count))