# -*- coding: utf-8 -*-

class Inzinjer:
    def __init__(self, ime, prezime, JMBG, licenca):
        self.ime = ime
        self.prezime = prezime
        self.JMBG = JMBG
        self.licenca = licenca

    def postaviIme(self, ime):
        self.ime = ime

    def postaviPrezime(self, prezime):
        self.prezime = prezime

    def postaviJMBG(self, JMBG):
        self.JMBG = JMBG

    def postaviLicencu(self, licenca):
        self.licenca = licenca

    def dajIme(self):
        return self.ime

    def dajPrezime(self):
        return self.prezime

    def dajJMBG(self):
        return self.prezime

    def dajLicencu(self):
        return self.licenca

    def info(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}".format(str(self.ime), str(self.prezime), str(self.JMBG), str(self.licenca))

class GeodetskiInzenjer(Inzinjer):
    def __int__(self, ime, prezime, JMBG, licenca, staz):
        Inzinjer.__init__(self, ime, prezime, JMBG, licenca)
        self.staz = staz

    def postaviStaz(self, staz):
        self.staz = staz

    def dajStaz(self):
        return self.staz

    def infoGI(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}, Broj staza: {4:s}".format(str(self.ime), str(self.prezime), str(self.JMBG), str(self.licenca), str(self.staz))

    def infoLicencaIG(self):
        a = self.dajLicencu()
        if a == 'None':
            print('Geodetski inzenjer nema licencu')
        else:
            print('Geodetski inzenjer ima licencu: ' + str(self.licenca))

class ElektrotehnickiInzenjer(Inzinjer):
    def __inin__(self, ime, prezime, JMBG, licenca, br_projekta):
        Inzinjer.__init__(self, ime, prezime, JMBG, licenca)
        self.br_projekta = br_projekta

    def postaviBrojProjekta(self, br_projekta):
        self.br_projekta = br_projekta

    def dajBrojProjekta(self):
        return self.br_projekta

    def infoIE(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}, Broj projekata: {4:s}".format(str(self.ime), str(self.prezime), str(self.JMBG), str(self.licenca), str(self.br_projekta))

    def infoLicencaIE(self):
        a = self.dajLicencu()
        if a == None:
            print('Elektrotehnicki inzenjer nema licencu')
        else:
            print('Elektrotehnicki inzenjer ima licencu: ' + str(self.licenca))

a = Inzinjer('Nemanja', 'Djordjevic', '1234', 'Geodetska')
a.info()

b = GeodetskiInzenjer('Nemanja', 'Djordjevic', '1234', 'Geodetska')
b.infoLicencaIG()

c = ElektrotehnickiInzenjer('Nemanja', 'Djordjevic', '1234', None ,)
c.infoLicencaIE()
