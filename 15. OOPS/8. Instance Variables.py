class Employee:
    company = "Android"  #Class Variable, associated with Class, we try to change a Class Variable, then it becomes Instance variable
    noofEmployees = 0
    def __init__(self, name):
        self.name = name
        self.salary = 100000  #Instance Variable, associated with Instances
        Employee.noofEmployees += 1
        self.employeeCount = Employee.noofEmployees #stores the number of counts and then increments
    def info(self):
        print(f"Employee name is {self.name} who works in {self.company} and salary is {self.salary} and total employees are {self.employeeCount}")
        
obj1 = Employee("Aaryan")
Employee.company = "Yahoo"
print(Employee.company)
obj2 = Employee("Rohan")
obj2.company = "Google"
obj2.salary = 250000
obj1.info()
obj2.info()

obj3 = Employee("ada")
obj3.info()


