# -*- coding: utf-8 -*-

a = raw_input('Unesi p ili d: ')
niz1 = [1, 2, 3]
niz2 = [5, 10, 15]

if a == 'p':
    niz = [None]*(len(niz1)+len(niz2))
    niz[::2] = niz1
    niz[1::2] = niz2
    print niz
elif a == 'd':
    niz = [None]*(len(niz1)+len(niz2))
    niz[::2] = niz2
    niz[1::2] = niz1
    print niz
