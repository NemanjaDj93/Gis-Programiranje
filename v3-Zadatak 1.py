# -*- coding: utf-8 -*-
import math

class Sfera:
    objekti = 0
    def __init__(self, x = 0, y = 0, z = 0, r = 1):
        self.z = z
        self.r = r
        self.x = x
        self.y = y
        Sfera.objekti = self.objekti + 1

    @staticmethod
    def brojObjekata():
        return Sfera.objekti

    def zapreminaSfere(self):
        v = (self.r)
        return (4 / 3) * v ** 3 * math.pi

def testSfera():
    print(Sfera.brojObjekata())
    sfera = Sfera(0, 0, 0, 4)
    globus = Sfera(1, 1, 1, 12)
    bilijarska_lopta = Sfera(10, 10, 10, 10)
    jedninicna_sfera = Sfera()
    print(Sfera.brojObjekata())
    print('Zapremina sfere je ' + str(sfera.zapreminaSfere()))
    print('Zapemina globusa je ' + str(globus.zapreminaSfere()))
    print('Zapremina birijalske lopte je ' + str(bilijarska_lopta.zapreminaSfere()))
    print('Zapremina jedinicne sfere je ' + str(jedninicna_sfera.zapreminaSfere()))

testSfera()
