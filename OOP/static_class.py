class Math:
   def __init__(self):
      return
   
   # static methods don't need ojects
   # They can be called at any point whether there's an instance of of the class or not
   @staticmethod   
   def add5(x):
      return x + 5
   
   @staticmethod
   def pr():
      print("run")

print(Math.add5(5))
Math.pr()

"""
class Person:
   number_of_people = 0
   
   def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.add_person()
      
   def show(self, name):
      name = name
      print(f"I am {name}")
         
   @classmethod   
   def number_of_people_(cls):
      return cls.number_of_people() 
   
   @classmethod
   def add_person(cls):
      cls.number_of_people += 1 

class Manager(Person):
   def lead(self):
      return "He is an executive "     
   
class Employee(Person):
   def work(self):
      return "He is an employee "   
   
Person.number_of_people = 8

p = Person("Jay", 12)   
print(p.number_of_people)  
print(p.show("Tim")) 
print(Person.add_person())
"""