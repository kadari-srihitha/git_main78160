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