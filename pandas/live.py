import numpy as np
import matplotlib.pyplot as plt
y1 = 0.5
x1 = 0.1
z1 = 9.8
for i in range(1000):
    y = np.random.random()
    x = np.random.random()
    z = np.random.random()
    x1 += x
    y1 += y
    z1 += z
    print("{} , {} ".format(x1,y1))
    plt.grid(True)
    plt.axvline()
    plt.axhline()
    plt.plot(x1,np.sin(z1),'r.-')
    plt.plot(y1,np.cos(x1),'b.-')
    plt.plot(z1,np.cos(y1),'k.-')
    plt.pause(0.05)

while True:
    plt.pause(0.05)

"""
x = 0.008
y = 0.456
z = 9.8

"""