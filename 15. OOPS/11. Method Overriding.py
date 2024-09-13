#Same Method but in different classes is called method overriding

from math import pi

class Rectangle:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Rectangle):
    def __init__(self, r):
      self.radius = r
      super().__init__(self.radius, self.radius)
    def area(self):
        return pi * super().area()
    
obj1 = Rectangle(2, 3)
area = obj1.area()

obj2 = Circle(5)
area2 = obj2.area()
print(area)
print(area2)