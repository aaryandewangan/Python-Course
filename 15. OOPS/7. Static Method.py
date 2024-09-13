class Sum:
    def __init__(self, value):
        self.value = value
    def addition(self, n):
        self.value = self.value + n
        
obj1 = Sum(2)
add = obj1.addition(3)
print(obj1.value)

#Static Method is used to remove self from a Method, making the code small, For example -

class Math:
    @staticmethod
    def add(a, b): # Static Method
        return a+b
obj2 = Math()
sum = obj2.add(2, 3)
print(sum)