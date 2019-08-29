import numpy as np 

a=np.linspace(1,12,6)

print a # arreglo del 1 al 12 saltando de 2.2 en 2.2


print a.reshape(3,2)

print a.size #cantidad de elmentos del arreglo

print a.shape # entrega (3,2)

print a.dtype #tipo de datos dentro del arreglo

print a.itemsize #8 bytes de memoria

