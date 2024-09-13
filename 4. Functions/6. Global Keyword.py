x = 5 #global variable

def global_Keyword():
    global x # It is used when we want to access same variable as outside the function
             # It can be used to change the outside variable to another value
    x = 8 # Now the value of x is changed, so it will print '8' instead of '5' and can be used outside the function also
    
    y = 2 # Local Variable
    print(y)
    
global_Keyword()
print(x) # '8' is printed instead of '5'  we successfully changes the value of global variable from inside the function