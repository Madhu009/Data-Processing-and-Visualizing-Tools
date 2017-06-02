import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np

# simulates input from serial port
def random_gen():
    while True:
        val = random.randint(1,10)
        yield val
        time.sleep(0.50)


a1 = deque([0]*20) # create a queue of 0's length =10
ax = plt.axes(xlim=(0, 20), ylim=(0, 10))
d = random_gen()

print(a1)
line, = plt.plot(a1,marker="o")
plt.ion()
plt.show()
t=1

for i in range(0,20):
    a1.appendleft(next(d))# add random value(0,10:d) to the queue
    datatoplot = a1.pop() #pop the last index value(FCFS)
    line.set_ydata(a1) #set y data with x being 0,1,2,3....
    plt.draw()
    print(a1[0])
    print(a1)
    i += 1
    time.sleep(0.1)
    plt.pause(0.001)

print("done")
