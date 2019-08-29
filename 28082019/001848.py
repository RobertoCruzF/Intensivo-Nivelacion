import numpy as np 


# array con numero del 0 al 9
a= np.arange(10)

print a

# imprime el array a con los valores ordenadas aleatoriamente
np.random.shuffle(a)
print a


# elige un valor aleatorio dentro de los elmenentos de a
print np.random.choice(a)

# imprime un array con dos valores aleatorios entre 5 y 10
print np.random.random_integers(5,10,2)

