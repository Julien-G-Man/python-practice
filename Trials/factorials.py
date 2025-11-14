# finding the factorial of a number n

def find_factorial(n):
   n_factor = 1
   for i in range(1, n+1):
      i += 1
      n_factor *= i
      print(f"{i} factorial = {n_factor}")
      if i == n:
         print(f"\nFinal Answer: {n} factorial = {n_factor}")
         exit()   

   return f"\nFinal Answer: {n} factorial = {n_factor}"     

n = 10 #int(input("Number: "))

if __name__ == "__main__":
   find_factorial(n)
   
