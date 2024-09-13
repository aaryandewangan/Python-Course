#Multilevel inheritence is deriving class from a Child class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed
    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")
        
class Goldenretriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed = "Goldenretriever")
        self.color = color
    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")
        
obj = Goldenretriever("Tommy", "Golden")
obj.show()
 