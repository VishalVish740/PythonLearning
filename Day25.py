# Day79 --> Miltiple inheritance
class Employee:
    def __init__(self,name):
        self.name = name

    def Show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def Show(self):
        print(f"The dance is {self.dance}")
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

obj = DancerEmployee("Break-Dance","Vishal")
print(obj.name)
print(obj.dance)
obj.Show()
print(DancerEmployee.mro())  #Method resolution order

# Day80 -->Multilevel inheritance (parent class -> child class -> child class)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

dog = GoldenRetriever("Max", "Golden")
dog.show_details()