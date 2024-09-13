choice = int(input(" What you want to do - \n 1. Encrypt \n 2. Decrypt \n 3. Exit \n Your Choice: "))

#Encryption...

newword = []

if choice == 1:
    n = input("Enter the message: ")
    words = n.split(" ")
    for i in words:
        if(len(i)>=3):
            random1 = "ade"
            random2 = "gtr"
            
            encrpt = random1 + i[1:] + i[0] + random2
            newword.append(encrpt) #converting string to list 
        else:
            newword.append(i[::-1])
    print(" ".join(newword))  #cconverting list to string back
    
    
# Decryption...

elif choice == 2:
    n = input("Enter the message: ")
    words = n.split(" ")
    for i in words:
        if(len(i)>=3): 
            decrypt = i[3:-3]
            main_decrypt = decrypt[-1] + decrypt[0:-1]
            newword.append(main_decrypt) #converting string to list 
        else:
            newword.append(i[::-1])
    print(" ".join(newword))  #cconverting list to string back
    
else:
    exit()