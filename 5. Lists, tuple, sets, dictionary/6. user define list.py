list = []

n = int(input("Enter the Number of Elements: "))

for i in range(n):
    a = int(input())
    list.append(a)

print(list)


# To take inputs in 1 line - 

l = []

l = list(map(int, input("Enter the Elements with spaces: ").split()))

print(l)