n = int(input("Enter the value between 5 and 9: "))

if(n<5 or n>9):
    raise ValueError("Error! Not an integer value or not between 5 and 9")
else:
    print(n)