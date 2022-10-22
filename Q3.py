#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:00:37 2022

@author: ml
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,1,2,3,4,5])
ypoints = np.array([2,4,6,14,10,12])

plt.plot(xpoints,ypoints,marker = 'D', linestyle = '--', color='red', ms=10, mec='green', mfc='green')
plt.show()