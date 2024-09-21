# Strings in python
name = "Vishal"
print("Hello " + name)

# Printing multiline strings
fruits = '''Apple
Banana
Papaya
Guvava
Pear
'''
print(fruits)

for character in name:
    print(character)

# String Slicing means use to start and stop the string charcacter -- Create a slice object. This is used for extended slicing
names = "Welcome to College"
print(names[0:7])
print(names[:7])
print(names[0:])
print(names[0:-4])

# String Methods --> Strings are immutable in python
name_str = "Vishal!!!!  Vishwakarma!!"
print(len(name_str))
print(name_str.upper())
print(name_str.lower())
print(name_str.rstrip("!"))

# Split method
print(name_str.split(" "))

# Methods
na = "vishal,vishal"
print(na.capitalize())
print(na.center(50))
print(na.count("vishal"))
print(na.find('l'))
print(na.swapcase())
print(na.startswith('vi'))
print(na.endswith('al'))