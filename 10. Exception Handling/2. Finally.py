def function():
    try:
        list = [1,2,3,4,5]
        n = int(input("Enter the Index Number: "))
        print(list)
        print(list[n])
        
        return "Executed Properly"
    except:
        return "Some error occured !!"
        
    finally:
        print("Finally keyword - I am always executed no matter what the error is") #finally can be printed in functions also while 
                                                                                    #print statement doesnt work in functions in Exception Handling
            
x = function()
print(x)