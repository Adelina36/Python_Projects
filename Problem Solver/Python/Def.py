# def es una función

def tabla_de_multiplicar(n):
    for i in range(1,11):
        print(n,'*',i,'=',i*n)

tabla_de_multiplicar(5)


def cadena():
    return 'Python'
print(cadena())


n = 5
def funcion():
    print(m)
m = 10
funcion()


def dato():
    n = 2
    print(n)
dato()
n = 4
dato()
print(n)

def suma(a,b):
    return a + b
respuesta = suma(4,8)
print(respuesta)

# separar una lista en pares e impares
ejemplo = [3,7,9,5,8,3,7,12]

def separar_lista(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares
pares,impares = separar_lista(ejemplo)
print(pares)
print(impares)