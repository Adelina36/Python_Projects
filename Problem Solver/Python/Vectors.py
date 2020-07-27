# Vectores (arreglos)

n = int(input('Ingrese el tamaño del arreglo: '))
m = int(input('Ingrese el número de múltiplos: '))
a = []
for i in range(0,n):
    a.append(i*m)
print(a)

# arreglos
# EJEMPLO: [1,4,2,8,6,2,8,9,10]

# Imprimir por pantalla los números impares a 3

a = [1,4,2,8,6,2,8,9,10,30,13]
b = []
for i in a:
    if i > 3 and i % 2 != 0:
        b.append(i)
print(b)

# arreglos
# calcular 10 números aleatorios

import random

def vector_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(0,10)
    return vector
print('Ingrese cuántos números aleatorios desea obtener: ')
n = int(input())
aleatorio = vector_aleatorio(n)
print(aleatorio)
