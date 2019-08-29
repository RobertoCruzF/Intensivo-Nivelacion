import numpy as np 

# defino el arreglo
a=np.array([3,-1,-2,4,-6,8])

print a # imprimo el arreglo

print a<0 # reccore array, imprime array de true o false si se cumple o no la condicion


negatives=a<0 # valores menores a 0 del arreglo a

print a[negatives] # imprime arreglo con los valores negativos del arregloa

print a[a<0]# imprime arreglo con los valores negativos del arregloa

a[a<0]=0

print a # reemplaza los valores negativos dentro de a po numeros 0


print a<8 # reccore array, imprime array de true o false si se cumple o no la condicion


print a>3 # reccore array, imprime array de true o false si se cumple o no la condicion

print (a<8).any() # si hay un valor menor a 8 dentro del arreglo imprime true , osino, false

print (a>3)&(a<8) # reccore array, imprime array de true o false si se cumple o no la condicion

f=6
g=9
print f+g # imprime la suma de ambas variables

print f.__add__(g) # a f se le suma g









