# Day 17 --> For Loop in python
for i in range(1,101):
    print(i, end=",")

print('\n printing colors')
colors = ['\nRed','White','Blue','Pink']
for c in colors:
    print(c)

# While Loop
i = 1
while(i<=4):
    print(i)
    i = i + 1

print("\nPrinting Decrement while loop")
count = 5
while(count > 0):
    print(count)
    count = count - 1

# Break and Continue Statement
for table in range(12):
    if(table == 10):
        break
    print("5 X", table+1, "=", 5 * (table+1))

# Continue statement
print("\nprinting continue statement")
for table in range(12):
    if(table == 10):
        print("Skip the iteration")
        continue
    print("5 X", table, "=", 5 * (table))   