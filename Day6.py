# Day 14 --> if elif else conditional statement
# > , < , == , >= , <= ,!=

age = int(input("Enter Your Age:"))
print("Your age is",age)

if(age >= 18):
    print("You can drive")
elif(age >= 60):
    print("You are old can not drive")
else:
    print("You can not drive")

#Day15--> Match Case Statement
x = int(input("Enter Value of x:"))
match x:
    case 0:
        print("x is zero")
    case 5:
        print("case is 5")
    case _:
        print("Default case",x)
