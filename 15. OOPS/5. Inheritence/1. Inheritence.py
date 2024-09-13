class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"The Id of emplyee {self.name} is {self.id}")
        
class Programmer(Employee):
    def language(self):
        print("Using Python Language")
        
obj = Employee("Rohan", 11)
obj.details()

obj2 = Programmer("Shoham", 22)
obj2.details()
obj2.language()