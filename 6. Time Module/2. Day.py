import time

hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

if(hour<12 & hour>=0):
    print("Good Morning !")
elif(hour<17 & hour>=12):
    print("Good Evening !")
else:
    print("Good Night !")