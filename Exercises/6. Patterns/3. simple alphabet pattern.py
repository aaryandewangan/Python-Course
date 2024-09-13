rows = int(input("Enter the Number of rows: "))

ascii = 65

for i in range(0, rows+1): 
    for j in range(0, i):
        
        alpha = chr(ascii)   
        print(alpha, end = " ")
        ascii += 1
    print()