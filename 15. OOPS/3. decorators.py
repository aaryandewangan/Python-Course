def greet(fx):     #fx - function
    def mfx():     #modified function - mfx
        print("Good morning !")
        fx()
        print("Thank you for using it !")
    return mfx

@greet
def hello():
    print("Hello World......")
    
hello()