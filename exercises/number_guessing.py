import random

def main():
   print("Welcome to the number guessing game!")
   max_number = int(input("Enter a max number: "))
   print(f"I'm thinking of a number between 1 and {max_number}. Can you guess it?")
   
   secret_number = random.randint(0, max_number)
   
   attempts = 0
   while True:
      guess = int(input("Enter your guess: "))
      attempts += 1
   
      if guess > secret_number: 
         print("Too high. Try again.")
         
      elif guess < secret_number:
         print("Too low, try agin.")
      else:
         print(f"Congrats! You got the correct answer {secret_number} in {attempts} attempts.") 
         exit()  
      
if __name__ == "__main__":
   main()   
   