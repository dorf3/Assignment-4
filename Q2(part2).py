#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:55:09 2022

@author: ml
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3,6,9,12])
ypoints = np.array([2,8,1,10])

plt.plot(xpoints,ypoints,marker = 'o')
plt.show()