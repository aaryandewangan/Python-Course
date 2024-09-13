def fil(a):
    return a>4

li = [1,2,3,4,5,6]
a = list(filter(fil, li))
print(a)