# -*- coding: utf-8 -*-

a1 = int(input('stepeni 1'))
b1 = int(input('minuti 1'))
c1 = int(input('sekunde 1'))

a2 = int(input('stepeni 2'))
b2 = int(input('minuti 2'))
c2 = int(input('sekunde 2'))

pravac1 = a1 + float(b1)/60 + float(c1)/3600
pravac2 = a2 + float(b2)/60 + float(c2)/3600

ugao = round((pravac2 - pravac1), 4)

print(pravac1)
print(pravac2)

if ugao >= 0:
    print(ugao)
else:
    print (ugao + 360)
