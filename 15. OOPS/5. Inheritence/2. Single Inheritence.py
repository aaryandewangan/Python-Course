class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def animal_sound(self):
        print(f"The sound made by animal")
        
class Dog(Animal):
    def __init__(self, name, species,  breed):
        super().__init__(name, species)
        self.breed = breed
    def animal_sound(self):
        print("Bark")
        
obj = Dog("dog", "dog", "doberman")
obj.animal_sound()

obj2 = Animal("dog", "dog")
obj2.animal_sound()