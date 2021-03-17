# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:07:03 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np

num_pontos = np.linspace(1, 100, 100)
xcos = np.cos(2*3.14*num_pontos/20)

ycos = np.cos(2*3.14*num_pontos/10)

soma_ponto_a_ponto = []
for i in range(len(num_pontos)):
    soma_ponto_a_ponto.append(xcos[i]+ycos[i])

plt.plot(num_pontos, soma_ponto_a_ponto, label='duas senoides')

plt.legend()

plt.show()
