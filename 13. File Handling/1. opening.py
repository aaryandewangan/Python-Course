# r - read
  #-> rt - read in text
  #-> rb - read in binery form, in bytes, opens images and other non-text file
# w - write
# a - append (adding extra content)
# f.close - very important to close you are doing before starting another. Example- if you are reading a file, close it forst to open the file in write or append mode

f = open("test.txt", "r")
print(f)

text = f.read()
print(text)
f.close()

f = open('test.txt', 'w')
f.write("Writing from python, writing overrides the contents that were already there")
f.close
# "Use me as a test file" - was already writen in the text file, but due to write keyword, 
# the content was replaced by the content i provided in f.write()

#However if you dont want to change the content and add other things we use append.

f = open('test.txt', 'a')
f.write("Adding extra text")
f.close