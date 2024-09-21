#Day61--> Inheritance
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showData(self):
        print(f"The name of employee: {self.id} is {self.name}")

e1 = Employee("Vishal",432)
e1.showData()

# inheriting the parent class
class Programmer(Employee):
    def showLang(self):
        print("The default language is python")
emp = Programmer("Virat",64)
emp.showLang()

# Day62 --> Access Modifier -- are use to limit the class within instance
# Public,Private,Protected
class Student:
    def __init__(self):
        self.name = "Vishal"

a = Student()
print(a.name)

#Day65--> Static methods() -- used when we don't need instance of class
class Math:
    def __init__(self,num):
        self.num = num

    def addnum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b
# No need to pass self in class method
a = Math(5)
print(a.num)
a.addnum(6)
print(a.num)

# Using static method
print("Using static method:", a.add(3,4))
print("Using static method with class name:", Math.add(5,4))