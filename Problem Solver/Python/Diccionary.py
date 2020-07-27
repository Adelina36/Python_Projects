# DICCIONARIO

edades = {'David': 30,'Carlos':60,'Víctor':34,'Héctor':30}
print(edades)
for i in edades:
    print(i,edades[i])


# DICCIONARIO CON FUNCIONES
notas = {'David':30,'Carlos':40,'Víctor':50}
print(type(notas))
print(notas.clear())

notas_2 = notas.copy
print(notas_2)

# notas_3 = {'David':30,'Carlos':40,'Víctor':50}
notas_3 = dict.fromkeys(['David', 'Carlos', 'Víctor'],100)
print(notas_3)

notas = {'David':30,'Carlos':40,'Víctor':50}
valor = notas.get('Carlos')
print(valor)
items1 = notas.items()
print(items1)
keys = notas.keys()
print(keys)

dic_1 = {'a':1,'b':2,'c':3,'d':4}
dic_2 = {'d':5,'e':6}
dic_1.update(dic_2)
print(dic_1)
value = dic_1.values()
print(value)
value = dic_1.pop('c')
print(value)
print(dic_1)