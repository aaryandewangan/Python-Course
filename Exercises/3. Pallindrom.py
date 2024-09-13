num = int(input("Enter a value: "))

temp = num
rev = 0

while( temp > 0 ):
    l_digit = temp % 10
    rev = rev * 10 + l_digit
    temp //= 10
    
if(num == rev):
    print("Pallindrom number")
else:
    print("Not pallindrom")