#in split, we cannot call integer variables, so we use map
a, b, c = map(int, input().split())
d, c= map(int, input().split())
print (a+b+c+d)