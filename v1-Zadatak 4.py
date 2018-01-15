# -*- coding: utf-8 -*-

a = int(input('Prvi broj:'))
b = int(input('Drugi broj:'))

x = 0

while b > 0:
    y = b % 10
    b = b // 10
    x = x + y

cifre = []

while a > 0:
    cifre.append(a % 10)
    a = a // 10

par = cifre[1] + cifre[3]
nepar = cifre[0] + cifre[2]

razlika = par - nepar

print(x)
print(razlika)