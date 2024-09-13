class MyClass:
    def __init__(self, value):
        self.value = value
    def show(self):
        print(f"{self.value} is the value")
        
    @property
    def ten_value(self):       #Getter
        return 10*self.value 
    
    @ten_value.setter          #Setter, we do not return anythin in Setter
    def ten_value(self, new_value):
        self.value = new_value/10
        
obj = MyClass(10)
obj.ten_value = 30
print(obj.ten_value)
obj.show()