# readLines

f = open("test2.txt", "r")

i=0
while True:
    i = i+1
    
    lines = f.readline()
    if not lines:
        break
    
    marks1 = lines.split(",")[0]
    marks2 = lines.split(",")[1]
    marks3 = lines.split(",")[2]
    
    print(f"Marks of student {i} in OS: {marks1}")
    print(f"Marks of student {i} in Maths: {marks2}")
    print(f"Marks of student {i} in Scinece: {marks3}")
    
    print(lines)
    

