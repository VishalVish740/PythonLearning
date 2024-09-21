# Day59 --> Decorators- is function that takes another function as an argument returns a new function 
# that modifies the behaviour of another function.
def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Welcome to college")
    return mfx

@greet
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)
hello()
add(3,5)

# Day60 --> Getters() and setters() method are use to access the values of an object properties.
# Getters()
class myClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value of {self._value}")

    def ten_value(self):
        return 10* self._value
    
    @property
    def ten_value(self):
        return 10*self._value

obj = myClass(10)
print(obj.ten_value)
obj.show()

# Setter()
class myClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value of {self._value}")

    def ten_value(self):
        return 10* self._value
    
    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

obj = myClass(10)
obj.ten_value = 100
print(obj.ten_value)
obj.show()