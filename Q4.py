#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:09:29 2022

@author: ml
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,4])
ypoints = np.array([1,5])
zpoints = np.array([5,9])
mpoints = np.array([9,13])

plt.plot(xpoints, ypoints)
plt.plot(xpoints, zpoints)
plt.plot(xpoints, mpoints)

plt.show()