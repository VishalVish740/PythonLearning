# Day97 --> Multithreading in python
import threading
import time
# Normal method code
def funct(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)
funct(3)
funct(4)
funct(5)
# Using thread
t1 = threading.Thread(target=funct, args=[2])
t2 = threading.Thread(target=funct, args=[3])
t3 = threading.Thread(target=funct, args=[4])
t4 = threading.Thread(target=funct, args=[5])
t1.start()
t2.start()
t3.start()
t4.start()

# Day98 --> Multiprocessing
import multiprocessing
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Counter value:", counter.value)