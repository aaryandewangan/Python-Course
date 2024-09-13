with open("test4.txt", "r") as f:
    f.seek(10) #it starts reading the text from the 10th character instead of reading from start, 10th character is starting point now
    #print(f.read())
    
    print(f.tell()) #tells from which character the code starts / tells where is seek
    
    print(f.read(5)) #Reads next 5 bytes