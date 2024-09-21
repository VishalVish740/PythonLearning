#Day51--> Lambda functions is single expression values
from functools import reduce

def sum(x):
    return x+2
print(sum(4))

# using lambda function
double = lambda x: x*2
print("Using lambda function", double(5))

cube = lambda x: x * x * x
print(cube(3))

avg = lambda a,b: (a+b)/2
print(avg(5,4))

#Day53--> map(),filter(),reduce()
# map()-->Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
list1 = [1,2,3,4,5,3,2]
newl = list(map(cube,list1))
print(newl)

# Filter()--> Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
def filter_function(a):
    return a>4
newli = list(filter(filter_function,list1))
print(newli)

# Reduce() -->Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single.
from functools import reduce
number = [1,4,7,3,9]

def mysum(x, y):
    return x+y
sum = reduce(mysum,number)
print(sum)

# Day54--> is and "==" both is comparison operator
# is will give exact location and == will give value
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)