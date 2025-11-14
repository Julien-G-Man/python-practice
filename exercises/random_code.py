import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(F"Alphabet: {alphabet}")
print(len(alphabet))

letters = [a for a in alphabet]
print(f"Alphabet letters: {letters}")

char = [random.choice(letters) for let in range(6)]
print(f"Random characters for code: {char}")

code = ""
for i in char:
    code += i

print(f"\nCode: {code}")