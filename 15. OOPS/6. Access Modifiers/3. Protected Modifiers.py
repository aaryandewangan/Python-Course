#for private modifier, the prefix is '_'

class Employee:
    def __init__(self):
        self._name = "Aaryan"       
    def _hello(self):
        return "Learning Python"
        
obj = Employee()
print(obj._name)      #printing protected Variable
print(obj._hello())   #printing protected Method