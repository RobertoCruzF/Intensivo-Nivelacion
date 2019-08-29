import numpy as np 


a=np.arange(24).reshape(6,4) # matriz de 6X4 con valores del 0 al 23

print a.shape # imprime las dimensiones de la matriz a

print a.mean(axis=0).shape # cantidad de columnas de la matriz

print a.mean(axis=1).shape # cantidad de filas de la matriz

channel_means=a.mean(axis=1)

