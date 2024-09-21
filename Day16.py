#Day45--> if __name__=="__main__"
def welcome():
    print("Hello welcome to college")

print(__name__)
if __name__ == "__main__":
    welcome()

# Day46--> OS module
'''
import os
os.mkdir("Hello")   #TO make directory
os.getcwd()   #TO get current working directory
os.rename("Hello","Welcome")  #TO rename directory
os.chdir("/Users")   #TO change directory
os.remove("Hello")   #TO remove directory
'''
# Local and Global
x = 5
def my_func():
    # global x
    x = 4
    y = 7
    print(y)

my_func()
print(x)