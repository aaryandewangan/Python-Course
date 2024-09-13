class Person:
    name = "Aaryan"
    age = 21
    course = "IT"
    
    def info(self):  #self is an instance of a class
        print(f"{self.name} is {self.age} years old")

obj = Person()

name = obj.name
age = obj.age
course = obj.course

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")

obj.info()  # calling a function inside of a class

obj2 = Person()
obj3 = Person()

obj2.name = "Ram"
obj2.age = 13

obj3.name = "Shyam"
obj3.age = 25

obj2.info()
obj3.info()