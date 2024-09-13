import os
import pathlib as path

if not os.path.exists:  #creates sub folder if "data" folder exists
    os.mkdir("data")

for i in range(1, 21):
    os.mkdir(f"data/Day {i}")
    
    
#get current directory

