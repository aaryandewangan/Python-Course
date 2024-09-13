rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2
  
for i in range(rows-1,-1,-1):    
        for j in range(m,0,-1):  
            print(end=" ")
        m += 1 
        for j in range(0, i+1): 
            print("*",end=" ")              
        print()