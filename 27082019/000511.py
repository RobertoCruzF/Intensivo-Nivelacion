import numpy as np 

#z1 son 6 numreos random del 1 al 10 con semilla 0
np.random.seed(0)
z1=np.random.randint(10,size=6)
print z1 #imprime array

print z1[0] #imprime primer valor del arrray

print z1[0:2] # imprime primeros dos valores del array

print z1[-1] # imprime ultimo valor del array