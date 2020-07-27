# Módulo

from math import pi
a = pi
print(a)

from math import factorial
a = factorial(6)
print(a)

from math import log
a = log(10,100)
print(a)

from random import choice
a = choice(['Cara','Cruz'])
print(a)

from random import randrange
a = randrange(100)
print(a)

from datetime import date
dia = date(2020,5,17)
año = date(2020,12,31)
fin_de_año = (año - dia).days
print('Faltan ',fin_de_año)

from fractions import Fraction
a = Fraction(2,4)
b = Fraction(4,8)
print(Fraction(a+b))



