num = int(input("Enter the value:"))
n1, n2 = 0, 1

n3=0
for i in range(0, num):
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n1+n2    