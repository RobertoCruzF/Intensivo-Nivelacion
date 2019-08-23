# genera la lista give_list2
given_list2=[5,4,4,3,1,-2,-3,-5]
# define la variable
total5=0

i=0

# Ejecuta lo que esta dentro del while siempre que el valor que va recorriendo de la lista given_lista2 sea 
# positivo, avanzando con el indice i el cual aumenta en uno cada iteracion del while, si el elemento dentro
# de la lista given_list2 es negativo, el while deja de ejecutarse. De no existir esta condicion, se crea 
# un ciclo infinito.

while True:
	# suma al valor de la variable total5 el valor del elemento de la lista given_list2 en el indice i de esta misma
	total5+=given_list2[i]


	i+=1

	if given_list2[i]<=0:
		break


# imprime el valor de la variable total5
print total5