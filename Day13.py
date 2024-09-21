# Day33--> Dictionary in python are ordered collection of data items
dict = {'Name':'Vishal','Age':23,'Address':'Mumbai'}
print(type(dict))
print(dict.keys())
print(dict.values())
print(dict)

# Dictionary methods in python
emp = {12:40 , 15:50, 18:60, 20:70, 30:100}
emp2 = {31:50, 35:70, 60:90}
emp.update(emp2)
print(emp)

#Day34--> For loop with else
for i in range(6):
    print(i)
else:
    print("Sorry no i")
