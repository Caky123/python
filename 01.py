
class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__ (self, typ):
        super().__init__()
        self.typ = typ
    
    def haf(self):
        print(f"{self.__name} haf!")
    
    def change_name(self, name):
        if(self.__name != "Petr"):
            self.__name = name


my_dog = Dog("Max", 10, "savec")
my_dog.haf()

my_dog.change_name("Petr")
my_dog.haf()



