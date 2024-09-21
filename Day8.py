# Day20 --> Functions in python
def add(x,y):
    print(f"Addition of {x} and {y} is {x+y}")
add(4,5)

# printing function with string variable
def name(fname, lname):
    print("Hello,", fname, lname)
name("Vishal", "Vishwakarma")

# Default Argument
def average(a=5,b=5):
    print("The average is",(a+b)/2)
average()

# Other Method
def average(a,b):
    print("The average is",(a+b)/2)
average(3,4)

# Keyword Argument
def average(a=3,b=4):
    print("The average is",(a+b)/2)
average(b=5,a=4)

# Required Argument
def average(a,b,c=2):
    print("The average is",(a+b+c)/2)
average(3,4)

# Printing name by using dictinory
def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
name(mname="Vishal",lname='Vishwakarma',fname="Vishal")