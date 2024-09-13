#for private modifier, the prefix is '_ _'

class Employee:
    def __init__(self):
        self.__name = "Aaryan"       
        
obj = Employee()
print(obj._Employee__name)  # To access Private Modifier use the syntax - 'obj._(className)__(privateVariable)', 
                            #this is called Name Mangling
