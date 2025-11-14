"""
You have a list of names. Create a list of names that start with the letter 'C'

Expected output:
['Charlie']
"""

names = ["Alice", "Bob", "Charlie", "David"]
print(names[0][0])

starts_with_c = []
for name in names:
    if name.lower()[0] == 'c':
        starts_with_c.append(name)
print(starts_with_c)  
      
# short forms   
with_c = [name for name in names if name.lower()[0] == 'c']          
print(with_c)

c_names = [name for name in names if name.lower().startswith('c')]
print(c_names)