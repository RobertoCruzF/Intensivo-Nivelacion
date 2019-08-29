import numpy as np 


# se definen dos listas
a=[1,2,3,4]
b=[10,11,12,13]

# se suman las listas
print a+b

output=[]

#recorro listas a y b conjunjuntamente y le agrego la suma de cada elemento de cada lista en la lista output
for item1, item2 in zip(a,b):
	output.append(item1+item2)

# imprimo la lista con valores agregados
print output


# genera una lista del 1 al 1000000-1
g= list(range(1000000))

#print %timeit sum(g)


#print timeit np.sum(g_array)

print a

# se define el array con esos valores dentro
a=np.array([1,2,3,4])
 
# se define el array con esos valores dentro
b=np.array([10,11,12,13])

print a # imprimo arreglo
print b # imprimo arreglo

print a+b # suma de los dos arreglos

print a*b # multiplicacio de los arreglos

print a/b # division de los arreglos

print a**b  # elebe los valores de a con los elmentos dentro del arreglo b

print a.ndim # dimension del arreglo

print a.shape # cantidad de elementos dentro del arreglo a

f=5

print type(f) # tipo de dato de la variable f

f=(5,6)

print type(f)# tipo de dato de la variable f

print 10 # imprime 10

print 10, # imprime 10,

print a.shape # cantidad de elementos dentro del arreglo a

print a # imrpime arreglo

print b # imprime arrelgo

print a*10 # multiplica valores dentro del arrelgo por 10

print a*100 # multiplica valores dentro del arrelgo por 100

print np.sin(a) # funcion seno

print np.exp(a) # funcion exponencial

print np.log(a) #funcion logaritmo en base 10

print np.log # imprime tipo de funcion (logaritmo base 10)

print np.sum  # imprime tipo de funcion (suma)

print sum # funcion suma

print



