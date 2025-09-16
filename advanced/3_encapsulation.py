class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # Private attribute

    def check_password(self, pwd):
        return self.__password == pwd

u1 = User("john", "secure123")
print(u1.check_password("secure123"))  
print(u1.check_password("wrongpwd"))   
