# -*- coding: utf-8 -*-

#Do rezultata da li se tacka nalazi unutar trougla doslo se na osnovu
#toga da da li povrsina trougla ABC jednaka sumi povrsina trouglova
#ABD, ACD i BCD

x1 = int(input('Unesite x koordinatu tačke A:  '))
y1 = int(input('Unesite y koordinatu tačke A:  '))
x2 = int(input('Unesite x koordinatu tačke B:  '))
y2 = int(input('Unesite y koordinatu tačke B:  '))
x3 = int(input('Unesite x koordinatu tačke C:  '))
y3 = int(input('Unesite y koordinatu tačke C:  '))
x = int(input('Unesite x koordinatu tačke D:  '))
y = int(input('Unesite y koordinatu tačke D:  '))

def povrsina(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

A  = povrsina(x1, y1, x2, y2, x3, y3) #ABC
A1 = povrsina(x, y, x2, y2, x3, y3) #DBC
A2 = povrsina(x1, y1, x, y, x3, y3) #ADC
A3 = povrsina(x1, y1, x2, y2, x, y) #ABD

if (A == A1 + A2 + A3):
    print ('DA')
else:
     print ('NE')

