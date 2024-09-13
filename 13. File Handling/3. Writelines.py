#writing multiple lines

f = open("test3.txt", "w")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
f.writelines(lines)
f.close