#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:34:45 2022

@author: ml
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,1)
plt.bar(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([20, 30, 40, 50])
m = np.array([10,20,30,40])

plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.plot(x, m)

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.subplot(2, 3, 3)
plt.scatter(x, y)

plt.subplot(2,3,4)
y = np.array([35, 25, 25, 15])
mylabels = ["Purple", "Brown", "Pink", "Grey"]
plt.pie(y, labels = mylabels)
plt.pie(y)

plt.subplot(2,3,5)
x = np.random.normal(170, 10, 250)
plt.hist(x)

plt.subplot(2,3,6)
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.title("A")
plt.xlabel("B")
plt.ylabel("C")
plt.plot(x, y)
plt.grid()

plt.show()