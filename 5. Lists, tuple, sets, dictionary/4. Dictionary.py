name = {
    1: "Aaryan",
    2: "Adarsh",
    3: "Deep"
}

print(name)
print(name[1])

print(name.keys())
print(name.values())

d1 = {1: "Hi", 2: "how", 3: "are"}
d2 = {4: "You"}

d1.update(d2)
print(d1)

d1.pop(1) #removes any key-value
print(d1)

d1.popitem()  #removes last key-value
print(d1)