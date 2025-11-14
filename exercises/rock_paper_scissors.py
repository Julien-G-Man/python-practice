#Rock Paper Scissors Game
import random

def play():
   print("====== ROCK PAPER SCISSORS ======")
   print("Hi there! Welcome to the Rock-Paper-Scissors game.")
   
   user = input("Enter your username >>> ").capitalize()     
   computer = "ChatGPT" 
       
   print(f"Yo {user}! Ready to play? You'll be playing against {computer}. You can enter q anytime to quit.")
   
   options = ["rock", "paper", "scissors"] 
   
   user_score = 0
   computer_score = 0
   number_of_rounds = 10
   
   for i in range(1, number_of_rounds + 1):
      print(f"\nROUND {i}")
      computer_choice = random.choice(options)
      user_choice = input("Enter your choice >>> ")
      
      # use quits game
      if user_choice == "q":
         #declarre the one with the higher score as winner and exit
         if user_score > computer_score:
            print(f"\nGame Disrupted. {user} wins by default with {user_score} against {computer_score}")
         elif user_score < computer_score:
            print(f"\nGame Disrupted. {computer} wins by default with {computer_score} against {user_score}")
         else:
            print(f"\nGame Disrupted. Tie; {user_score} against {computer_score}")     
            
         print("Quitting...")
         exit()   # quit game
 
      print(f"{user} choice: {user_choice}")
      print(f"{computer} choice: {computer_choice}")
            
      # Tie
      if user_choice == computer_choice:
         print(f"\nIt's tie!")
         winner = None
       
      # User wins   
      elif user_choice == "rock" and computer_choice == "scissors":
         winner = user
         
      elif user_choice == "paper" and computer_choice == "rock":
         winner = user
         
      elif user_choice == "scissors" and computer_choice == "paper":
         winner = user
         
      # computer wins   
      else:
         winner = computer
   
      # Evaluating winner
      if winner == user:
         user_score += 1
         print(f"\n{winner} wins!") 
         print(f"{user} score = {user_score}, {computer} score = {computer_score}")
      elif winner == computer:                
         computer_score += 1
         print(f"\n{computer} wins") 
         print(f"{user} score = {user_score}, {computer} score = {computer_score}\n")    
          
      i += 1   # go to next round
      continue
   
   # Evaluating final winner
   if user_score > computer_score:
      print(f"\nFinal result: {user} wins with {user_score} against {computer_score}") 
      winner_score = user_score  
   elif computer_score > user_score:
      print(f"\nFinal result: {computer} wins with {computer_score} against {user_score}") 
      winner_score = computer_score
   else: 
      print(f"\nFinal Results: Tie. {user_score} againts {computer_score}")   

if __name__ == "__main__":
   play()
