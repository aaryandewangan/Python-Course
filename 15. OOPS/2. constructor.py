#constructors are called automatically when we call the 

class person:
    def __init__(self, name, age): #constructor
            self.name = name
            self.age = age
    def info(self):
        print(f"{self.name} is {self.age} years old.")       
         
a = person("Aaryan", 21)
b = person("Ram", 17)

a.info()
b.info()