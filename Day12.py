# Day31--> Sets in python is collection of well defined object
s = {2,3,4,5,2}
print(s)
print(type(s))

vishal = set()
print(type(vishal))

# Day32--> Sets method
a = {1,2,3,4,5}
b = {1,2,4,5,7}

city1 = {'Mumbai','Delhi','Noida','Banglore','Kerla'}
city2 = {'Mumbai','NCR','Noida','Chennai','Odisha'}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.isdisjoint(b))
print(a.issuperset(b))
print(city1.remove("Kerla"))
print(city2.discard("NCR"))
print(city1)

set1 = {1,2,3,9,4}
set2 = {1,2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))