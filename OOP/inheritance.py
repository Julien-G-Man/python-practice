# upper-level/parent class
class Pet: 
   def __init__(self, name, age):
      self.name = name
      self.age = age   
         
   def show(self):
      print(f"I am {self.name} and I am {self.age} years old.")

   def speak(self):
      print("I can't speak")

# child class inheriing from parent class (Pet)
class Cat(Pet):
   
   # adds an additional attribute
   def __init__(self, name, age, color):
      #but keeps these two values values from parent class
      super().__init__(name, age)
      self.color = color
      
   def speak(self):
         print("Meow!")
    
   def show(self):
      print(f"I am {self.name} and I am a {self.age} years old {self.color} cat.")
         
     
# child class inheriing from Pet           
class Dog(Pet):      
   def speak(self):
      print("Bark!")     
      
pet = Pet("Cutie", 10)     
pet.show()

cat = Cat("Milou", 5, "black")
cat.show()
cat.speak()

dog = Dog("Beki", 7)
dog.show()
dog.speak()
