# -*- coding: utf-8 -*-
import math

class Tacka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pomeriX(self, x_pomeraj):
        self.x = float(self.x) + x_pomeraj

    def pomeriY(self, y_pomeraj):
        self.y = float(self.y) + y_pomeraj

    def rastojanje(self, t):
        rastojanje = math.sqrt((self.x - t.x)**2 + (self.y - t.y))
        return rastojanje

class Duz:
    def __init__(self, p = 0, k = 0):
        self.p = p
        self.k = k

    def kreiranjeDuzi(self, x1, y1, x2, y2):
        p = Tacka(x1, y1)
        k = Tacka(x2, y2)
        d = Duz(p, k)
        return d
    def duzinaDuzi(self):
        return self.p.rastojanje(self.k)

    def str(self):
        print ('Pocenta x: ' + str(self.p.x) + ', Pocetna y : ' + str(self.p.y) + ', Krajnja x: ' + str(self.k.x) + ', Kranja y: ' + str(self.k.y))



def testGemetrija():
    x1 = raw_input('Koordinata X pocetne tacke: ')
    y1 = raw_input('Koordinata Y pocetne tacke: ')
    x2 = raw_input('Koordinata X krajnje tacke: ')
    y2 = raw_input('Koordinata Y krajnje tacke: ')

    pocetna = Tacka(x1, y1)
    krajnja = Tacka(x2, y2)

    a = Duz(pocetna, krajnja)
    b = Duz(pocetna, krajnja)
    duz1 = b.kreiranjeDuzi(0, 0, 6, 6)
    print(a.str())
    print(duz1.str())

    dx = float(raw_input('dx: '))
    dy = float(raw_input('dy: '))
    krajnja.pomeriX(dx)
    krajnja.pomeriY(dy)

    c = Duz(pocetna, krajnja)
    print(c.str())

testGemetrija()
