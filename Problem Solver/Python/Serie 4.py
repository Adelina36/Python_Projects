# serie fibonacci
ejemplo:
#w1+w2 = s
1 + 1 = 2
2 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13

n = int(input('Ingrese un número: '))
w1 = 1
w2 = 1
s = 0
c = 0
if n <= 0:
    print('Error')
elif n == 1
    print(w1)
else:
    while c < n:
        print(w1)
        s = w1 + w2
        # actualizar los datos
        w1 = w2
        w2 = s
        c = c + 1
