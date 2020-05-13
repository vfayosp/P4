
import numpy as np
import matplotlib.pyplot as plt


with open('lp_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,1)
plt.plot(c2)
plt.plot(c3)
plt.title("lp")
plt.show()

with open('lpcc_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,2)
plt.plot(c2)
plt.plot(c3)
plt.title("lpcc")
plt.show()

with open('mfcc_2_3.txt', 'r') as f:
    lines = f.readlines()
    c2 = [float(line.split()[0]) for line in lines]
    c3 = [float(line.split()[1]) for line in lines]

plt.subplot(3,1,3)
plt.plot(c2)
plt.plot(c3)
plt.title("mfcc")
plt.show()