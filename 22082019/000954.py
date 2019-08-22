
# Creo 2 listas vacias y una con un rango de 1 a 99
multcinco=[]

# crea la lista multtres y la lista de rango de 1 a 99
multtres=[]
lista= list(range(1,100))

# recorro la lista llamada "lista", luego aplico la condicion si el resto de el valor de la variable 
# recorrida dividida por 3 y por 5 se agrega el valor de de la lista a la lista multtres y multcinco
# respectivamente
for i in lista:

	if i%3==0:
		multtres.append(i)

	if i%5==0:
		multcinco.append(i)


# Se imprime en consola las listas multiplos de 5 , 3 y ademas una lista con los numero menores a 100
#, es decir todos los numeros.
print "Los multiplos de 5 son:", multcinco
print "Los multiplos de 3 son:", multtres

print "Los numeros que son menores a 100 son:",  lista