class Person:
   # allows us to instantiate the object right before usage
   def __init__(self, name, age): 
      self.name = name
      self.age = age
      print(name)
      
   def get_name(self):
      return self.name 
   
   def get_age(self):
      return self.age
   
   # attrubutes that modify existing attributes or create new attributes
   def set_name(self, name):
      self.name = name
      
   def set_age(self, age):
      self.age = age 
   
   def speak(self):
      name = "Mike"
      print(f"{name} is Speaking...") 
   
   
p = Person("Jay", 30)
print(p.get_name())
p.set_name("Mike")
p.set_age(9)
print(f"{print(p.get_name())}'s age is {p.get_age()}")
print(p.get_age())
print(p.speak())