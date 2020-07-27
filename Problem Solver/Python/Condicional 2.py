#califición de notas
#datos:
#n: notas
#r: respuesta

n = float(input('Ingrese su nota: '))
if n <= 5:
    r = 'Reprobado'
elif n <= 8:
    r = 'Aprobado'
elif n <= 9:
    'Sobresaliente'
else:
    r = 'Excelente'

print('Nota:',n, r)
