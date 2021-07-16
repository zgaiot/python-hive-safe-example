#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:24:50 2020

@author: w.wiyarungmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()