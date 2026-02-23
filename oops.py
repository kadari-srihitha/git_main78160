class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def speak(self):
        return f"{self.name} is speaking"
    

human1=human("srihitha",22)
human2=human("rishitha",23)
print(human2.name)
print(human2.age)
print(human1.speak())
# ENCAPSULATION
class human:
    def __init__(self,name,age,adhar):
        self.name=name
        self.age=age
        self.__adhar=adhar
    def get_adhar(self):
        pin=input("enter pin:")
        if pin=="123":
            print(self.__adhar)
        else:
            print("invalid pin")



human1=human("srihitha",22,12132456)
human1.get_adhar()

# #POLYMORPYSIM
class dog:
    def sound(self):
        return "bark"
class cat:
     def sound(self):
        return "meow"
dog=dog()
cat=cat()
print(dog.sound())
# print(cat.sound())
    
#INHERITENCE
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return f"{self.name} braks"
class dog(animal):
    def __init__(self,name,breed):
       super().__init__(name)
       self.breed=breed
ani=dog("buddy","blackship")

print(ani.name)
print(ani.breed)
print(ani.sound())

#ABSTRACTION
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "dog barks"
d1=dog()
print(d1.sound())
