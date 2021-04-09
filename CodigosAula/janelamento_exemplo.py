# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:54:42 2019

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

#constroi a janela de blackman
window = np.blackman(x_n.size)

#multiplica pelo sinal
x_window = window*x_n

n = len(x_n) # tamanho do sinal
k = np.arange(n) #vetor em k
T = n/Fs
frq = k/T # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))] # apenas um lado

X = np.fft.fft(x_n)/n # calculo da fft e normalização por n
X = X[range(int(n/2))]

X_window = np.fft.fft(x_window)/n
X_window = X_window[range(int(n/2))]

plt.subplot(221)
plt.title('Sinal')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.plot(t,x_n)

plt.subplot(222)
plt.title('FFT do Sinal')
plt.xlabel('f')
plt.ylabel('Magnitude')
plt.plot(frq,abs(X),'r')

plt.subplot(223)
plt.title('Sinal Janelado')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.plot(x_window)

plt.subplot(224)
plt.title('FFT do Sinal Janelado')
plt.xlabel('f')
plt.ylabel('Magnitude')
plt.plot(frq,abs(X_window),'r')

plt.show()