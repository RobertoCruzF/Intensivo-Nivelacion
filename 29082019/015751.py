import numpy as np 

# defino el array 
a= np.arange(25).reshape(5,5)


b= np.array([2,3,20])



print np.nan + 6 # imprime nan

print np.sum([1,np.nan,9]) # imprime nan

print np.nansum([1,np.nan,9]) # imprime 10

print a[a%3==0].sum() # suma de los valores dentro de a[a%3==0]


# defino el array
a= np.array([1,2,3])


print a # imprimo el array

print np.sum(a) # sumo los valores dentro del arreglo a

print a.sum() # sumo los valores dentro del arreglo a





