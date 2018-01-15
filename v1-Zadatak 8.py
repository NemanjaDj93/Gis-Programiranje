# -*- coding: utf-8 -*-
from random import randint

ime = str(raw_input('Ime: '))
broj = randint(0, 100)
unos = int(input('Unesi broj: '))
x = 1  #Broj pokusaja

while unos != broj:
    x = x + 1
    if unos < broj:
        unos = int(input('Pogresan broj, pokusajte veci broj: '))
    else:
        unos = int(input('Pogresan broj, pokusajte manji broj: '))

print('Pogodili se, trazeni broj je: ' + str(unos))
print('Broj pokusaja: ' + str(x))
