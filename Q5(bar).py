#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:31:01 2022

@author: ml
"""

from matplotlib import pyplot as plt
import numpy as np
 
marks = ['Andy', 'Amy', 'James', 'Jules', 'Arthur']
 
data = [88, 66, 90, 55, 77]

plt.bar(marks,data, width = .1)
plt.title('Grades')
plt.show()