# Day86 --> Walrus operator - it allows values to assign within parameter
a = True
print(a:=False)

# Example 
numbers = [1,2,3,4,5,6]
while(n := len(numbers)) > 0:
    print(numbers.pop())

# Without walrus operator
foods = list()
while True:
    food = input("What food do you like:?")
    if food == "quit":
        break
    foods.append(food)

# With walrus operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

# Day87 --> Shutil module
import shutil
shutil.copy("test.py","test2.py")
# shutil.copytree(".Python Learning","Learning")