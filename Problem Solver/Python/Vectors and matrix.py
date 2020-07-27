# vectores y matrices

import numpy as np

vector = np.array([6,7,1,2,3])
print(vector)
print(vector.astype(str))

a = np.array([6,7,1,2,3])
b = np.array([6,7,4,5,3])
print(a+b)
print(a<b)

vector = np.array([6,7,1,2,3])
print(vector[3])
print(vector.max())
print(vector.min())
print(vector.argmax())
print(vector.argmin())
print(vector.sum())
print(vector.prod())

vector = np.array([6,7,1,2,3])
matriz_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('vector: ',vector)
print(matriz_a)
print(matriz_a + matriz_b)
print('Vector: ',vector.size)
print('Matriz: ',matriz_a)
