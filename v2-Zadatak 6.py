# -*- coding: utf-8 -*-
import numpy as np

a = input('Broj tacaka: ')
x = []
y = []

i = 0

while i < a:
    x.append(input('x = '))
    y.append(input('y = '))

stepen = input('Stepen polinoma')
k = np.polyfit(x, y, stepen)
rez = np.polyfit(k)

print(rez)
