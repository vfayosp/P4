
import numpy as np
import matplotlib.pyplot as plt


with open('lp_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,1)
plt.plot(c2,'o')
plt.plot(c3,'o')
plt.title("lp")

with open('lpcc_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,2)
plt.plot(c2,'o')
plt.plot(c3,'o')
plt.title("lpcc")

with open('mfcc_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,3)
plt.plot(c2,'o')
plt.plot(c3,'o')
plt.title("mfcc")
plt.show()