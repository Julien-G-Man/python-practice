# Right angled triangle
print("# Right-angled triangle")
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()    
    
print("\n# Left-angled triangle")    
rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print() 
    
print("\n# Pyramid")       
rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()    
    