# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 07:23:46 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np

Fs = 40000;  # taxa de amostragem
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo

f = 100;   # frequencia do sinal
x1_n = np.sin(2*np.pi*f*t + 0)
f = 1000;
x2_n = np.sin(2*np.pi*f*t + 180)

x_n = x1_n + x2_n

n = len(x_n) # tamanho do sinal
k = np.arange(n) #vetor em k
T = n/Fs
frq = k/T # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))] # apenas um lado

X = np.fft.fft(x_n)/n # calculo da fft e normalização por n
X = X[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(X),'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')