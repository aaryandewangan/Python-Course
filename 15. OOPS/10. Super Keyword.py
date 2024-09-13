# Super keyword is used when u want to call a method of Parent class in Child class

class Parent_Class:
    def parent_method(self):
        print("This is PARENT CLASS")
    
class Child_Class(Parent_Class):
    def child_method(self):
        print("This is CHILD CLASS")
        super().parent_method()
        
obj = Child_Class()
obj.child_method()

#Example 2 - 

print("----------EXAMPLE 2----------")
class Employee():
    def __init__(self, name, id) -> None:
        self.name = name 
        self.id = id
        
class Extra(Employee):
    def __init__(self, name, id, lang) -> None:
        super().__init__(name, id)
        self.lang = lang
        
obj1 = Employee("Aaryan", 274)
obj2 = Extra("Aqua", 3802, "Python")

print(obj2.name)
print(obj2.id)
print(obj2.lang)