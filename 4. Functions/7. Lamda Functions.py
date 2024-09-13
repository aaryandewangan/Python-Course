#Lambda Function is like a function but in short form
from math import pow as p

# For Example (Normal Function) -
def cube(x):
    return p(x, 3)

a = cube(3)
print(a)

# Same example with Lambda Function - 
cube2 = lambda x: pow(x, 3)
print(cube2(3))

avg = lambda x, y: (x+y)/2
print(f"Average is: {avg(2,4)}" )


# function in function (Normal Function) -
def square(value):
    return value*value
def test(function, value):
    return 2 + function(value)

a = test(square, 4) 
print(a)

#but using lanbda function this code becomes very small

sqr = lambda x:x*x
output = lambda fun, x: 2+fun(x)
print(f"Using lambda function: {output(sqr, 4)}")