# -*- coding: utf-8 -*-

niz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
a = 0

for i in niz:
    a = a + 1  #Brojac pozicije elementa
    if a % 2 == 0:
        sum = sum + i

print(sum)
