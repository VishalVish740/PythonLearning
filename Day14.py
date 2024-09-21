#DAy36--> Exception handling in python
a = input("Enter the number:")
print(f"Multiplication of table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}  x {i} = {int(a)*i}")
# except :
#     print("Invalid Syntax")

except ValueError:
    print("Invalid Value")

except IndexError:
    print("Indexing error")

finally:
    print("Finally will execute in every case")

#DAy37--> Finally keyword 
def func():
    try:
        l = [1,3,4,6]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")

    finally:
        print("Finally will always executed")
f = func()
print(f)

#Day38--> Custom error
a = int(input("Enter value between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Value should be in range")
print("Executed")
