letter = "Hay! My name is {} and I am from {}"

name = "Aaryan"
country = "India"

a = letter.format(name, country)
print(a)

#print(f"") -> is a formula for f-string
print("\n")
print("------USING F-STRING------")
print(f"Hay! My name is {name} and I am from {country}")

price = 20.9999
print(f"This book is only for {price:.2f} RS")