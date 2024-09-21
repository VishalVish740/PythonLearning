# Day41 --> Short hand if else
a = 33000
b = 3340
print("A") if a > b else print("=") if a == b else print("B")

# Day42 --> Enumarate function is built-in function that allows to get the index and value at the same time.
marks = [12,35,56,76,88,95,45]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 5):
        print("Awsome") 

# Day43 --> Virtual environment in python
# pip freeze --> Will display all installed packages
# pip freeze > requirement.txt --> Will make txt file with all installed packages

# Day44 --> import in python is use to load a code
import math
print(math.floor(4.333))
print(math.sqrt(81))
print(math.sin(45))
print(dir(math))
