# using while loop

num = int(input("Enter a Number: "))
len = len(str(num))

sum = 0

temp = num
while temp>0:
    last_digit = temp % 10
    sum += last_digit ** len
    temp //= 10
    
if num == sum:
    print("Armstrong Number")
else:
    print("Not armstrong number")