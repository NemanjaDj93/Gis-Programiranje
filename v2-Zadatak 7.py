# -*- coding: utf-8 -*-
from random import randint

def spilKarata():
    broj = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    znak = ['herc', 'karo', 'tref', 'pik']
    spil = []

    for i in broj:
        for j in znak:
            spil.append(i + ' ' + j)
    return spil

def vrednostKarte(k):
    if k[:1] in ('1', 'J', 'Q', 'K'):
        return int(10)
    elif k[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        return int(k[:1])
    elif k[:1] == 'A':
        print ('Dobio si A')
        a = input('Da li zelis da se racuna kao 1 ili 11: ')
        while a != '1' or a != '11':
            if a == '1':
                return int(1)
            elif a == '11':
                return int(10)
            else:
                a = input('Da li zelis da se racuna kao 1 ili 11: ')

def novaKarta(spil):
    return spil[randint(0, len(spil)-1)]

def izbaciKartu(spil,karta):
    return spil.remove(karta)

igraj = ''
while igraj != 'Kraj' :
    ime = raw_input('Unesite svoje ime: ')
    spil = spilKarata()
    k1 = novaKarta(spil)
    izbaciKartu(spil, k1)
    k2 = novaKarta(spil)
    izbaciKartu(spil, k2)
    vr_k1 = vrednostKarte(k1)
    vr_k2 = vrednostKarte(k2)
    zbir = vr_k1 + vr_k2
    print('Imas karte ' + str(k1) + ' i ' + str(k2) +' to je ukupno ' + str(zbir) )

    #Karte koje dobija racunar
    kk1 = novaKarta(spil)
    izbaciKartu(spil, kk1)
    kk2 = novaKarta(spil)
    izbaciKartu(spil, kk2)
    vr_kk1 = vrednostKarte(kk1)
    vr_kk2 = vrednostKarte(kk2)
    r_zbir = vr_kk1 + vr_kk2
    print('Racunar ima kartu ' + str(kk1) + ' i jednu neodkrivenu kartu')
    print('Trenutni zibir karata racunara je: ' + str(vr_kk1))

    if zbir == 21:
        print('Blackjack, POBEDILI STE')
    else:
        while zbir < 21:
            a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne')")
            if a == 'da':
                nk = novaKarta(spil)
                izbaciKartu(spil, nk)
                vr_nk = vrednostKarte(nk)
                zbir = zbir + vr_nk
                print('Izvukli ste ' + str(nk) + ' sada je zbir ' + str(zbir))

                if zbir > 21:
                    print('IZGUBILI STE!')
                    igraj = input("Da li zlite ponovo? Ukoliko ne ukucajte 'Kraj'")

                elif zbir == 21:
                    print('POBEDILI STE!')
                    igraj = input("Da li zlite ponovo? Ukoliko ne ukucajte 'Kraj'")
                else:
                    continue
            elif a == 'ne':
                print('Racunar pokazuje svoju drugu kartu kartu')
                print('Druka karte je ' + str(kk2) + ' i zbir njegovih karata je ' + str(r_zbir))

                if r_zbir < 17:
                    print('Racunar dobija jos jednu kartu')
                    r_nk = novaKarta(spil)
                    izbaciKartu(spil, r_nk)
                    vr_r_nk = vrednostKarte(r_nk)
                    print('Racunar je dobio ' + str(r_nk))
                    r_zbir = r_zbir + int(vr_r_nk)

                    if r_zbir > 21 and zbir >= 21:
                        print('POBEDILI STE!')

                    elif r_zbir < 21 and r_zbir > zbir:
                        print('Racunar ima ' + str(r_zbir) + '. IZGUBILI STE!')

                    else:
                        continue

                elif r_zbir == zbir:
                    print('Nereseno je, nema pobednika')

                elif r_zbir < zbir:
                    print('POBEDLI STE')

                else:
                    print('IZGUBILI STE')

                igraj = input("Da li zlite ponovo? Ukoliko ne ukucajte 'Kraj'")
                break
