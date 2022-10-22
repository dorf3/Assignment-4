#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:06:03 2022

@author: ml
"""

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
for row in a:
    for n in row:
        print(n, end=' ')
    print()

flat_a = sum(a, [])
print(flat_a)