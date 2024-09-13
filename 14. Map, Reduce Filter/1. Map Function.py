from math import pow as p
def cube(x):
    return p(x,3)

n = int(input("Enter total Length of the list: "))
l = []

for i in range(n):
    ele = int(input("Enter Element 1 by 1 by presing enter:"))
    l.append(ele)
print(l)

newl = []
for item in l:
    a = cube(item)
    newl.append(a)
    
print(f"Cube of list is: {newl}")
    
#but instead of writing this big code we can use map for everything...
c = lambda x:pow(x,3)

li = [] 
li = list(map(int, input("Enter elements with spaces: ").split())) #creating a list

newli = map(c, li) #this gives mapped function
print(newli)

newli = list(map(c, li)) #this gives list output
print(f"Output after Mapping: {newli}")