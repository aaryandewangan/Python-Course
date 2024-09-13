def average(*numbers): # '*' is used to make a iterable tuple
    sum = 0  
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
    
a = average(5, 6, 7, 1)
print(a)