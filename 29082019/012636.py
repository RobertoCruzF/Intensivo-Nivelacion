import numpy as np 


print 0%2 # imprime el resto de la division de los dos numeros

print 1%2 # imprime el resto de la division de los dos numeros

print 2%2 # imprime el resto de la division de los dos numeros

print 3%2 # imprime el resto de la division de los dos numeros

print 4%2 # imprime el resto de la division de los dos numeros


# creo una matriz de 5X5 con valores desde el 0 al 24
a= np.arange(25).reshape(5,5)

print a # imprimo la matriz

print a%3 # imprimo la matriz con el el resto de la division por 3 de cada uno de los elmentos de la matriz 


print a[a%3] # multiplicacion del array a con la matriz  con el el resto de la division por 3 de cada uno de los elmentos de la matriz 



print a%3==0 # imprime la matriz a rellena de True o False dependiendo si se cumple la condicion 


print a[a%3==0] # imprime un array con valores dependiendo si se cumple o no la condicion

print np.nan # imprime nan

output= np.empty_like(a)

print output



output.fill(np.nan)

print output


output=np.empty_like(a,dtype='float')
print output


print a # imprime la matriz original


mask=a%3==0

output[mask]=a[mask]
print output

print np.where(a%3==0,a,np.nan)# imorime non en los valores de la matriz que ek resto no es0


print np.where(a%3==0,a,np.nan)


print a[mask]


print output[mask]

























