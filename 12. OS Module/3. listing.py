import os

dir = os.listdir("data")

for i in dir:
    print(i)
    
print(os.getcwd())#get current working directory