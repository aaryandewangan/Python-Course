x = 5 # global variable are made outside the function

def hello():
    x = 6 #here x is a global variable as same variable was used outside the function
    y = 1 #local variable - is only accessible inside the function
    
    print(f"Local variable is {y}")
    
hello()
print(f"Global variable is {x}")