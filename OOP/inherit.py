"""
Inheritance is a feature of object-oriented programming (OOP) that enables the transfer of methods and properties of one class to another. 
Inheritance allows for reusability of code as well as extending the capability of new classes.
"""

# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print({"Name": self.name, "Age": self.age})    
        
# child/derived class
class Student(Person):
    def __init__(self, name, age, program):
        super().__init__(name, age)
        self.program = program
        
        Person.__init__(self, name, age)
        
president = Student("Agyekum", 23, "Optometry") 
president.display_info()       