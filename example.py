from icecream import ic

class User:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        print("Getter")
        return self._username
    
    @username.setter
    def username(self, name):
        print("Setter")
        self._username = name if name != "" else "RANDOM"

    @username.deleter
    def username(self):
        print("Deleting username...")
        del self._username

user = User("")

# user.username = "jan"
ic(user.username)

del user.username
user.username = "jan"
ic(user.username)
