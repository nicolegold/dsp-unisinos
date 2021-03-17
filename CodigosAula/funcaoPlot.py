# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:07:03 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 40, 40)
plt.stem(x, np.cos(2*3.14*x/20), '-.')