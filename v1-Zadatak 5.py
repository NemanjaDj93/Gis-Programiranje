# -*- coding: utf-8 -*-

a = int(input('Petocifreni broj:'))

broj = []

while a > 0:
    broj.append(a % 10)
    a = a // 10

max = 0

for b in broj:
    if b > max:
        max = b

print(max)