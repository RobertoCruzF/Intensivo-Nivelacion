import numpy as np 

g=[1,2,3]


print g[0]  # imprime primer elemento de la lista g

print g[:1] # imprime primer elemento de la lista g


# matriz de dimensiones 5 X 5 con valores desde el 0 al 24
a= np.arange(25).reshape(5,5)

print a # imrime matriz

# matriz de  valores de la columna 2 y 3 de la matriz a
red=a[:,1::2]


print red # imprime matriz nueva


yellow=a[4] # arreglo de la ultima fila del arreglo a


yellow=a[-1] # arreglo de la ultima fila del arreglo a

yellow=a[-1:] # arreglo de la ultima fila del arreglo a dentro de otra lista

blue=a[1::2,:3:2] # arreglo con columnas 1 y 3 y filas 2 y 4


print id(a) # identificador del arrelgo

print id(red) # identificador del arrelgo

print red.flags # datos diccionario en red

print a.data # informacion del data


print red.coy()  # copia del array red

