from functools import reduce

a = lambda x, y: x+y

li = [1,2,3,4,5]
a = reduce(a, li)
print(a)
