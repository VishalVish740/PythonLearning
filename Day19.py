
# Day56--> OOPS
def hello():
    print("Welcome")
hello()

# Day57--> Classes and Object
class person:
    name = "Vishal"
    age = 23
    clas = 'Comp'

    def info(self):
        print(f"{self.name} is a {self.age}")
a = person()
print(a.name)
a.info()

#Day58--> Constructors will help you to make class.
class person:

    def __init__(self,n,o):
        print("Hello Welcome")
        self.name = n
        self.age = o
    
    def info(self):
        print(f"{self.name} is a {self.age}")
a = person("Vishal",24)
b = person
a.info()

# Parameterized Constructor --> takes parameter arguments
# Default Constructor --> self