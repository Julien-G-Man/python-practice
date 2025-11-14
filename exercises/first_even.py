"""
You have a list of numbers. Write a Python code to find 
and print the first even number greater than 10.
"""
# nevermind, was just trying to play around, lol.

numbers = [3, 7, 12, 5, 18, 9, 20, 45, 87, 32, 60, 100, 102]

def find_number():
   for num in numbers:
      if num > 10  and num % 2 == 0:
         print(f"The first even number greater than 10 is {num}.")
         position = numbers.index(num)+1
         order = get_order(position)
  
         print(f"{num} is found in the {position}{order} position.")
         break
      
def get_order(position: int):
   if position == 1:
      order = "st"
   elif position == 2:
      order = "nd"   
   elif position == 3:
      order = "rd"   
   else:
      order = "th" 
      
   return order  

if __name__ == "__main__":
   find_number()