# Day71 -->dir,__dict__,help method
from turtle import circle

x = [2,3,4,5,6,'hello']
print(dir(x))
print(x.__add__)
print("Printing Something", x.__imul__)
print(x.__delattr__)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 192.45
        self.vishal = "Vish"
p = Person("Vishal",23)
print("Printing dict method", p.__dict__)
print("Printing help method",help(Person))

# Day72 --> Super Keywords in python is used to refer a parent class
class ParentClass:
    def parent_method(self):
        print("This is parent class method")
    
class childClass(ParentClass):
    def parent_method(self):
        print("Something")
        super().parent_method()
    def child_method(self):
        print("This is child method")
        super().parent_method()

child_object = childClass()
child_object.child_method()
child_object.parent_method()

# Day73 --> Magic/Dunder method -- purpose to do some special task
print("\nDay 73 Started")
class Employee:
    name = 'Vishal'
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self) -> str:
        print("This is str method")

    def __repr__(self) -> str:
        pass

e = Employee()
print(e.name)
print(len(e))
print(type(repr))

# Day74 --> Method overriding- is concept of oops where a subclass provide a different implimentation of method that is already defined in super class
# We do overriding when parent class is redefined with the child class
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * super().area()

rec = Shape(3,4)
print(rec.area())

c = circle(105)
print(c)

# Day75--> Solution
