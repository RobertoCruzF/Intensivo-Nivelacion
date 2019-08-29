import numpy as np 



# arreglo del 1 al 12 saltando de 2.2 en 2.2

a=np.linspace(1,12,6)


print a<4 # imprime true o false dependiendo si el valor que recorre dentro del arreglo es menor o mayor a 4


print a*3 # imprime el arreglo a, con cada uno de sus elementos amplificado por 3


print a #imprime el arreglo original a

a*=3 #define un nuevo valor a a

print a # imprime el nuevo valor de el array a ya con los valores modificados


# immprime una matriz rellena de numeros ceros, de 4 columnas y 3 filas



a=np.zeros((3,4))
print a


print a.dtype # tipo de elementos dentro de la matriz


# martiz rellena de numeros unos, de 3 columnas y dos filas
a=np.ones((2,3))
print a

# matriz rellena de unos con 10 columnas y una fila (un array)
a=np.ones(10)
print a

# imprime un array con los valores dentro 2,3,4 y tipo de datos int 16 bytes
a= np.array([2,3,4], dtype=np.int16)

print a

# Imprime tipo de dato de los elementos dentro del array a
print a.dtype

print a.itemsize # 2 bytes, muy eficiente en terminos de memoria


# matriz de 2 filas y 3 columnas con numeros aleatorios entre 0 y 1
a=np.random.random((2,3))
print a

# imprime la matriz anterior pero aproximado cada numero con maximo 2 decimales
np.set_printoptions(precision=2, suppress=True)
print a

# array de 5 elementos con numeros aleatorios entre 0 y 10
a=np.random.randint(0,10,5)
print a


# imprime la suma de los elementos dentro de la matriz/array
print a.sum()

# imprime el valor minimo dentro del array
print a.min()

# imprime el valor maximo dentro del array
print a.max()

# imprime el promedio de los numeros dentro del array
print a.mean()

# imprime la varianza de los numeros dentro del array
print a.var()

# imprime la desviacion estandar de los numeros dentro del array
print a.std()

# array de 6 elementos con numeros aleatorios entre el 1 y el 10
a= np.random.randint(1,10,6)
print a

# matriz de 3 filas y dos columnas de los elementos dentro de a
a= a.reshape(3,2)
print a


# suma cada uno de los ejes x de la matriz

print a.sum(axis=1)


# suma cada uno de los ejes y de la matriz
print a.sum(axis=0)





















