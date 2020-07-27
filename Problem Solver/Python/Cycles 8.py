#la suma de los primeros n números

n = int(input('Ingrese un número: '))
suma = 0
for i in range (1, n +1):
    suma = suma + i
print('La suma de los n números hasta ',n,'es',suma)