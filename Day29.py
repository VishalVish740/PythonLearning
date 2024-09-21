# Day90 --> Exercise NEWS API'S 
# Day91 --> Gererator function is used in python to generate on the fly value and (yield keyword is used)
def my_generator():
    for i in range(50):
        yield i
gen = my_generator()
# printing particular value when required which value to print
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# printing all values
for j in gen:
    print(j)

# Day92 -->Function Caching
from ast import pattern
from cgitb import text
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(0.5)
    return n*5

print(fx(20))
print("Done for 20 ")
print(fx(2))
print("Done for 2 ")
print(fx(6))
print("Done for 6 ")
# Will compute computed value faster
print(fx(20))
print("Done for 20 ")
print(fx(2))
print("Done for 2 ")
print(fx(6))
print("Done for 6 ")
# Day 93 & 94 was solution and question

# Day95 -->Regular Expressions
import re
pattern = "The"
text = "The Quick Brown Fox Jump Over The Lazy Dog"
match = re.search(pattern,text)
print(match)

# Day96--> AsyncIO
import time

def function1():
    time.sleep(3)
    print("Function 1")

def function2():
    time.sleep(3)
    print("Function 2")

def function3():
    time.sleep(3)
    print("Function 3")

function1()
function2()
function3()

import asyncio

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

    L = await asyncio.gather(
                my_async_function(),
                my_async_function(),
                my_async_function(),
            )
    print(L)    
asyncio.run(main())

   