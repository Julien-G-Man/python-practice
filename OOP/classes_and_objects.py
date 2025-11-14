# Classes and Objects in Python
class Myclass:
    x = 10
p1= Myclass()
print(p1.x)    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#    def display(self):
#        print(f"Name: {self.name}, Age: {self.age}")

name = input("Enter your name: ")
age = input("Enter your age: ")
p1 = Person(name, age)    
print("Name: ", p1.name)
print("Age: ", p1.age) 
#del p1 
print(p1)  