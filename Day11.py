# Day28--> Python f-string
letter = "My name is {} and i am from {}"
country = "India"
name = "Vishal"
print(letter.format(name,country))   #using formate function

print(f"My name is {name} and i am from {country}")  #Using printf function

a = 5
b = 6
print(f"Addition of {a} and {b} is {a+b} \nAnd we have successfully executed printf function")

# Day29--> Docstrings and PEP-8
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**5)
square(5)
print(square.__doc__)

# PEP-8 Python enhancement proposal

# Recursion in python
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print("Factorial is",factorial(5))

# Using normal method
def calc():
    x = int(input("Enter Number:"))
    fact = 1
    if(x==0 and x==1):
        print("Yes")
    else:
        for i in range(1, x+1):
            fact = fact*i
        print(f"Factorial of {x} is {fact}")
calc()
