"""

"""

class UserInfo:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def  check_username(self, username_to_check):
        if username_to_check == self.username:
            print(f"Your username is {self.username}")
            return True
        else:
            print(f"This username is incorrect")   
            return False     
        
user = UserInfo("Julien", "julien@pivota.app")        
print(user.username, user.email)
user.check_username("Julien")