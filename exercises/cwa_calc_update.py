# Code for finding CWA of a Student (KNUST standard)
import statistics as stx
from statistics import mean
import math

print("******* CWA Calculator ********")  

def get_data():
   # each data is put in a list embedded into a dictionary
   subjects = {
      'name': [],
      'score': [],
      'credit': [],
      'id': [],
      'grade': []
   }
   num_subjects = int(input("How many subjects do you offer? "))

   p = 0 # position in list (like index)
   
   for i in range(num_subjects):
      print("----------------------------------------------------")
      n = i+1
      name = input(f"Subject #{n}: ")
      score = float(input(f"{name} Score: "))
      credit = int(input(f"{name} Credit: "))
      
      if score > 70:
         grade = "A"
      elif score > 60:
         grade = "B"  
      elif score > 50:
         grade = "C" 
      elif score > 40:
         grade = "D" 
      else:
         grade = "E"
    
      # each list is then updated with every new entry as last element in the list
      subjects["name"].insert(p, name)
      subjects["score"].insert(p, score)
      subjects["credit"].insert(p, credit)
      subjects["id"].insert(p, n)
      subjects["grade"].insert(p, grade)
      p += 1
      
   return calculate_cwa(subjects)    
  
  
def get_class(cwa):
   if cwa >= 70:
      student_class = "First Class Honours"
   elif cwa >= 60:
      student_class = "Second Class Upper"  
   elif cwa >= 50:
      student_class = "Second Class Lower" 
   elif cwa >= 40:
      student_class = "Third Class" 
   else:
      student_class = "Failed"
   
   return student_class  
   
   
def calculate_cwa(subjects):        
   total_weighted_score = sum(score * credit for score, credit in zip(subjects["score"], subjects["credit"]))
   total_credits = sum(sub for sub in subjects["credit"])

   if total_credits == 0:
       print("Total credits cannot be zero.")
   else:
      cwa = total_weighted_score / total_credits
      print("\n|=============== Results Summary ================|")
      print("---------------------------------------------------------")
      print("ID  Subject                 Credit     Mark       Grade")
      print("---------------------------------------------------------")
      
      for name, score, credit, id, grade in zip(subjects["name"], subjects["score"], subjects["credit"], subjects["id"], subjects["grade"]):
         s = 50 - len(subjects["name"])
         space = [" " for i in range(s)] 
         print(f"{id}   {name}{space}{credit}           {score}       {grade} ")
        
      print("---------------------------------------------------------\n")
      print(f"Total weighted score ..............: {total_weighted_score}")
      print(f"Cummulative Weighted Average (CWA).: {cwa:.2f}")
      print(f"Class .............................: {get_class(cwa)}")    
   
if __name__ == "__main__":
   get_data()   