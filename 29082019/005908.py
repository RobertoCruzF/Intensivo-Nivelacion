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

print np.nonzero(negatives) # imprime un array con los numeros positivos del arreglo a

print a.sort()

# defino los array con los valores definidos
a= np.array([10,1,20])

b= np.array([2,3,20])

print a>b # compara cada uno de los valores de a con los valores de b si cumple con la condicion, imprime true en caso contraroio false


print np.nonzero(a>b) # el unico que cumple con la condicion es 20-20=0


# defino array

a= np.array([10,1,20])

print a 

# defino nuevo array con valores dentro, de primer elemento del array a y el ultimo elemento
subset=a[[0,2]]

print subset # impprime nuevo valor de array
 

print a.flags.owndata # imprime True
 

print subset.flags.owndata # imprime True


print a is subset # imprime false, dado que borra el data


print a # imprime array a

print subset # array definido anteriormente


subset[0]=-1 # asigno un valor al primer valor del array subset

print subset # imprimo nuevo subset modificado

a[-1]= 100 # asigno nuevo valor al primer elmento del array a

print a # imprimo nuevo array a, ya modificado


a[negatives]=0 # los valores negativos dentro del array a, toman valor cero








