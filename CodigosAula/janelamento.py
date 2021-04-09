# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:38:53 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np

#window = np.hanning(51)
#window = np.hamming(51)
window = np.blackman(51)

plt.plot(window)
plt.title("Barlett window")
plt.ylabel("Amplitude")
plt.xlabel("n")
plt.show()
