#using more than 1 parent class in child class

class Employee:
    def __init__(self, name) -> None:
        self.name = name
    
class Dancer:
    def __init__(self, dance) -> None:
        self.dance = dance
        
class Child(Employee, Dancer):
    def __init__(self, name, dance) -> None:
        self.name = name
        self.dance = dance
        
obj = Child("Aqua", "Kathakali")
print(obj.name)
print(obj.dance)