"""
You have a list of numbers. Write  Python code to:
1. Find the index of the first occurence of 25
2. Insert 35 at index 2
3. Remove the last item
4. Copy the list
5. Clear all items from the original list
"""

numbers = [10, 25, 30, 45, 25, 60]
print(f"Original list: {numbers}")
# 1
index_25 = numbers.index(25)
print(f"\nIndex of 25: {index_25}")

# 2
numbers.insert(2, 35)
print("\nInserting 35 at index 2...")
print(f"New list: {numbers}")

# 3 
print(f"\nRemoving last item ({numbers[-1]}...)")
#numbers.remove(numbers[-1])
numbers.pop()
print(f"New list: {numbers}")

# 4
new_list = numbers.copy()
print("\nCopying list...")
print(f"Copied List: {new_list}")

# 5
print("\nClearing all items from the original list...")
numbers.clear()
print(f"Original list is now empty: {numbers}")