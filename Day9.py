#Day22--> List in python
list1 = ['name','age',12,'ram']
print(type(list1))
print(list1)
print(list1[len(list1)-3])

if "age" in list1:
    print("Yes")
else:
    print("No")

print(list1[:])    #Printing all list values

# Day23--> List Method
l1 = [2,3,4,5,6,7,9]
print(l1.append(1))
print(l1.index(1))
print(l1.sort(reverse=True))
l1.insert(1,1)
print(l1.count(3))
print(l1)