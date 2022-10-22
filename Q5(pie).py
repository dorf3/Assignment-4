#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:16:51 2022

@author: ml
"""

from matplotlib import pyplot as plt
import numpy as np
 
marks = ['Andy', 'Amy', 'James', 'Jules', 'Arthur']
 
data = [88, 66, 90, 55, 77]

fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = marks)
plt.legend(title = 'Legend', bbox_to_anchor=(1.05,1.0), loc='upper left')
plt.title('Grades')
plt.show()