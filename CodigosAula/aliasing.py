# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:49:48 2020

@author: jeans
"""
import matplotlib.pyplot as plt
import numpy as np

Fs = 10000;  # taxa de amostragem
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo
f = 800;   # frequencia do sinal
x1_n = np.cos(2*np.pi*f*t)

plt.plot(t,x1_n)

Fs = 600
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo
x2_n = np.cos(2*np.pi*f*t)


plt.plot(t,x2_n)

plt.xlim(0, 0.01)

plt.show()