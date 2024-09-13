try:
    n = int(input("Enter the value: "))
    print(f"Multiplication Table of {n} is -")
    for i in range(1,11):
        res = n*i
        print(f"{n} x {i} = {res}")

except ValueError:
    print("ERROR !! Not an integer input")
    
print("End of program")