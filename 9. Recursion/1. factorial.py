def factorial(n):
    if(n == 1 or n==0):
        return 1
    else:
        return n*(factorial(n-1))
    
n = int(input("Enter a Value: "))
fact = factorial(n)
print("Factorial of", n, "is: ", fact)