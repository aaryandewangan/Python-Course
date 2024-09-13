class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 1000000
        
    def info(self):
        print(f"His name is {self.name} and age is {self.age}")
        
a = Employee("Aaryan", 21)
a.info()
print(a.__dict__)

print(help(a)) #Tells everything about a
