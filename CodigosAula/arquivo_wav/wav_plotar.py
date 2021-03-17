# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:07:03 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np
import wave as fw

arqff = 'sin_100Hz_1s.wav';
arquivoWav = fw.open(arqff, 'r');

print("Número canais: ", arquivoWav.getnchannels());
print("Número bytes: ", arquivoWav.getsampwidth());
print("Taxa de amostragem: ", arquivoWav.getframerate());
print("Número de frames: ", arquivoWav.getnframes());
print("Compactação: ", arquivoWav.getcompname());

tipos = np.uint8;
Damp = 256;
if arquivoWav.getsampwidth()>1:
    tipos = np.int16;
    Damp = 32760;

frames = arquivoWav.readframes(-1);
Amplitude = np.fromstring(frames, tipos)/Damp;
fim = np.size(Amplitude);
fim2 = round(fim/2 - 1);

dt = 1.0 / arquivoWav.getframerate();
tempo = np.arange(0, arquivoWav.getnframes() * dt, dt);
arquivoWav.close();

plt.plot(tempo, Amplitude); plt.grid();
plt.title(arqff);

plt.show();


