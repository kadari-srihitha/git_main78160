# class human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


#     def speak(self):
#         return f"{self.name} is speaking"
    

# human1=human("srihitha",22)
# human2=human("rishitha",23)
# print(human2.name)
# print(human2.age)
# print(human1.speak())
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


