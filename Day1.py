#Day1--> To write single line comment in python use # and for multiline comment use ''' '''

#Day2--> Escape Sequence characters

print("Hello Welcome to college \nIf you not present then you will be mark as absent")  # \n is use for escape sequence

# Escape sequence characters
print("Hello World", 7, 9, sep="~")  #Seperator
print("Hello World", 7, 9, end="009\n") #End 

for table in range(15):
    if(table == 10):
        break
    print("5 X", table+1, "=", 5 * (table+1))
