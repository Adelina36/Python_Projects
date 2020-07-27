# del & in

curso = 'Python'
lista_nueva = list(curso)
print(lista_nueva)

del lista_nueva[0]
print(lista_nueva)

print('y' in curso)

print('a' in lista_nueva)

if 'a' in lista_nueva:
    print('Y es parte de la lista')
