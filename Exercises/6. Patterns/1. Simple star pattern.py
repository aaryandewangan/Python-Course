rows = int(input("Enter the Number of rows: "))

for i in range(0, rows+1):  #Outer for loop to handle number of rows 
    for j in range(0, i+1):  #Inner for loop to handle number of columns  
                             #values change according to the outer loop  
        print("*", end = " ")  #end is used for spaces
    print() #End line after each row (creating Next line)