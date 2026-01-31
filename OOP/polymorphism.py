"""
Polymorphism in OOP is the concept of classes sharing methods with the same name. 
This becomes useful when there are objects initiated from different classes that may share similar methods.
In Python, classes are allowed to contain methods that share the same name as another method from a different class. 
"""

class Checking():
    def type(self):
        print("You have a checking account")
        
    def balance(self, amount):
        print(f"You have ${amount} in your checking account")   
        
class Savings():
    def type(self):
        print("You have a savings account")
        
    def balance(self, amount):
        print(f"You have ${amount} in your savings account")    
        
        
checking_account = Checking()
savings_account = Savings()

for account in (checking_account, savings_account):
    account.type()
    account.balance(1000)
    print("")