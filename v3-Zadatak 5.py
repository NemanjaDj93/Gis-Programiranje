# -*- coding: utf-8 -*-
from datetime import datetime

class Osoba:
    def __init__(self, ime, prezime, datum_rodjenja, adresa):
        self.ime = ime
        self.prezime = prezime
        self.datum_rodjenja = datum_rodjenja
        self.adresa = adresa

    def postaviIme(self, ime):
        self.ime = ime

    def postaviPrezime(self, prezime):
        self.prezime = prezime

    def postaviDatimRodjenja(self, datum_rodjenja):
        self.datum_rodjenja = datum_rodjenja

    def postaviAdresu(self, adresa):
        self.adresa = adresa

    def info(self):
        print "Ime:{0:s}, Prezime:{1:s}, Datum rodjenja:{2:s}, Adresa:{3:s}".format(str(self.ime), str(self.prezime), str(self.datum_rodjenja), str(self.adresa))

class Djak(Osoba):
    def __init__(self, ime, prezime, datum_rodjenja, adresa, skola = 'Jovan Jovanovic Zmaj', odeljenje = 'IV-2', god_upisa = '1999'):
        Osoba.__init__(self, ime, prezime, datum_rodjenja, adresa)
        self.skola = skola
        self.odeljenje = odeljenje
        self.god_upisa = god_upisa

    def razred(self):
        a = str(self.odeljenje)
        b = a.split('-')
        return b[0]

    def obnavljanje(self):
        a = 8  #trajanje skolovanja
        b = self.god_upisa
        studiranje = 2018 - int(b)
        if studiranje <= a:
            print('Djak nije obnovio godinu')
        else:
            print('Djak je obnvovio godinu')

class Zaposleni(Osoba):
    def __init__(self, ime, prezime, datum_rodjenja, adresa, kompanija, departman, datum_zakljucenja = '1.1.2018', datum_prekida = '1.1.2018'):
        Osoba.__init__(self, ime, prezime, datum_rodjenja, adresa)
        self.kompanija = kompanija
        self.departman = departman
        self.datum_zakljucenja = datum_zakljucenja
        self.datum_prekida = datum_prekida

    def dajRadniStaz(self):
        v = datetime.now()  #trenutni datum i vreme
        g = v.year
        m = v.month
        a = self.datum_zakljucenja
        b = self.datum_prekida
        dat_zak1 = a.split('.')
        dat_zak2 = b.split('.')
        m1 = int(dat_zak1[1])
        g1 = int(dat_zak1[2])
        m2 = int(dat_zak2[1])
        g2 = int(dat_zak2[2])
        br_meseci1 = (g - g1)*12 + (m - m1)
        br_meseci2 = (g2 - g1)*12 + (m2 - m1)
        if dat_zak2 == None:
            print ('Ukupni radni staz u mesecima iznosi: ' + str(br_meseci1))
        else:
            print('Ukupni radi staz u mesecima iznosi: ' + str(br_meseci2))


#Djak

a1 = raw_input('Ime djaka: ')
a2 = raw_input('Prezime djaka: ')
a3 = raw_input('Datum rodjenja: ')
a4 = raw_input('Adresa: ')
a5 = raw_input('Skola: ')
a6 = raw_input('Odeljenje: ')
a7 = raw_input('Godina upisa: ')

a = Djak(a1, a2, a3, a4, a5, a6, a7)
print ('Razred djaka je: ' + str(a.razred()))
print (a.obnavljanje())

#Zaposleni

b1 = raw_input('Ime zaposlenog: ')
b2 = raw_input('Prezime zaposlenog: ')
b3 = raw_input('Datum rodjenja: ')
b4 = raw_input('Adresa: ')
b5 = raw_input('Ime kompanije: ')
b6 = raw_input('Ime departmana: ')
b7 = raw_input('Datum zakljucenja: ')
b8 = raw_input('Datum prekida: ')

b = Zaposleni(b1, b2, b3, b4, b5, b6, b7, b8)
print(b.dajRadniStaz())




