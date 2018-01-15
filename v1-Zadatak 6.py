# -*- coding: utf-8 -*-

a = unicode(raw_input('Pet karaktera:'))

sum = 0

for b in a:
    if b.isdigit():
        sum = sum + 1

print(sum)