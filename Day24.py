# Day77 --> Operator Overloading
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j 
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(2,4,5)
print(v2)

# Day78 --> Single inheritance - where child class extend the properties of single parent class
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,breed,name):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow")

d = Dog("Dog","Kutta")
d.make_sound()

a = Animal("Dog","Puppy")
a.make_sound()

c = Cat("Meow","Billi")
c.make_sound
