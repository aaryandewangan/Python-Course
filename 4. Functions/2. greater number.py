def isGreater(a,b):
    if(a>b):
        print(a, "is greater than", b)
    elif(a<b):
        print(b, "is greater than", a)
    else:
        print("Both are equal")
    
a = int(input("Enter A: "))
b = int(input("Enter B: "))
isGreater(a,b)