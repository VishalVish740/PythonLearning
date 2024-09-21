# File Handling in python File IO
# Reading file 
f = open('file.txt','r')
text = f.read()
# print(text)
f.close()

# Writing to a file
'''
w = open('file2.txt','w')
w.write("Hello")
w.write("\nWelcome")
w.close()
'''

#50--> Other Methods
# read()
# readline()
# readlines()
# writable
x = open('file.txt','r')
t = x.readlines()
print(t)
x.close()

#51--> seek(),tell() and other function
with open('file.txt','r') as f:

    f.seek(10)
    print(f.tell())  #returns the current position within the file in bytes
    data = f.read(5)
    print(data)

# truncate used to 