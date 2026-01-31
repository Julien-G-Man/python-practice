"""
Access modifiers are used to control or restrict access to members, also known as variables and methods, within a class. 
These modifiers play an important role in limiting access to secure the members within the class. 

The three access modifiers within Python:
    - Public Access Modifiers
    - Protected Access Modifiers
    - Private Access Modifiers
"""

# PUBLIC
"""
By default, all members within a class are public, and there’s no need to specify access modifiers for public members. 
Being public means that these members can easily be accessed outside of the class, in another part of the program.
"""

class ClassSchedule:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        print("Class schedule created")
        
    def display_course(self):
        print(f"Coourse: {self.course}")
        print(f"Instrcutor: {self.instructor}")

# All members here are accessible outside of the class. 
# For example, we can access the variable course and method display_course() without any limitations:

schedule = ClassSchedule("Math", "Prof. Smith")
schedule.display_course()

# PROTECTED
"""
Protected access modifiers, denoted with the prefix _, prevent members from being accessed outside of the class, unless it’s from a subclass. 
Let’s modify the class from the example above and make the members course and instructor protected with the _.
"""

class TutorialSchedule:
    def __init__(self, course, instructor):
        self._course = course # protected
        self._instructor = instructor # protected
        print("\nTutorial schedule created")
        
    def display_course(self):
        print(f"Coourse: {self._course}")
        print(f"Instrcutor: {self._instructor}")

# The variables course and instructor are now protected members in the class.
Tusched = TutorialSchedule("Computing", "Prof. David")
Tusched.display_course()


# PRIVATE
"""
Private access modifiers, denoted with the prefix __, declare members to be accessible within the class only. 
Members with this modifier will be marked private and any attempt to access these members outside of the class will cause an Attribute Error message.
"""

class PracticalSchedule:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
       print("\nPractical schedule created")
  
   def display_course(self):
       # public
        print(f"Course: {self.__course}")
        print(f"Instrcutor: {self.__instructor}")
 
sched = PracticalSchedule('programming', 'Ms. Smith')
 
try:
    sched.__course # this will throw an Attribute Error because we're trying to access a private member
except Exception as e:
    print(f"Error: {e}")    
 
sched.display_course() # this won't throw an Attribute Error because this method is public