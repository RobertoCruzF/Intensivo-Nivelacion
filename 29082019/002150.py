import numpy as np 
 
a=np.array([1,2,3,4]) # define el arreglo con valores dentro

print a.dtype # tipo de valor del arreglo junto con sus bytes, int dado que son numeros naturales

a= np.array([1,2,3,4.0]) # define el arreglo con valores dentro


print a.dtype # tipo de valor del arreglo junto con sus bytes, flotatnte dado que hay decimales

a= np.array([1,2,3,4.0+1j]) # define el arreglo con valores dentro


print a.dtype # tipo de valor del arreglo junto con sus bytes

a= np.array([1,2,3,4.0], dtype='int32') # define el arreglo con valores dentro


print a.dtype # tipo de valor del arreglo junto con los bytes definidos dentro del arreglo


a= np.array([1,2,3,4.0]) # define el arreglo con valores dentro


print a.dtype # tipo de valor del arreglo junto con sus bytes definidos por default


c= np.array([[10,11,12],[20,21,22]]) # defino el arreglo matriz de 3 columnas y dos filas

print c # imprimo


print c.dtype # tipo de valores del arreglo c por default

print c.shape # dimensiones del arreglo c

print a.T # arreglo transpuesto

print c.size # cantidad de elemntos dentro del arreglo


print c.nbytes # numero de bytes
 
print a[0] # primer valor dentro del arreglo a


a[0]=10 # defino nuevo valor al primer valor del arreglo a


print a # imprimo nuevo valor del arrglo a 


print c[0,0] # imprimo primer valor del arreglo c dentro de la primer sublista dentro del arrglo

print c[0] # imprimo primer sublista, arreglo dentro del arreglo principal c


print 





























