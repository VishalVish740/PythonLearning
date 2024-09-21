# Day81 -->Hybrid and Hierarchical Inheritance - BasedClass used by many class
class BaseClass:
    print("This is Base Class")
class DerivedClass(BaseClass):
    print("This is derived Base Class")
class Derived2(BaseClass):
    print("This class is derived from parent class and base class")
class Derived3(Derived2,DerivedClass):
    print("This is class derived from every class")

# Day82 --> Solution Merge PDF

# Day84 --> Time Module in python
import time
def usingwh():
    i = 0
    while i<1000:
        i = i + 1
        print(i)

def usingfor():
    for i in range(1000):
        print(i)
init = time.time()
usingwh()
t1 = (time.time() - init)

init = time.time()
usingfor()
print(time.time() - init)
print(t1)

# Day85 --> Command Line Utility
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()
print(args.optional)