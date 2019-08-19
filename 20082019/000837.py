# define la funcion la cual en primer lugar imprime en consola el valor de la variable
# del input, luego imprime "still in this function", termina retornando el valor de la 
# variable del input multiplicada por 3. Todo esto claramente cuando se evalua la funcion4


def function4(x):
	print x
	print "still in this function"
	return 3*x


# se define la variable "f", como la funcion4 evaluada con la variable4

f= function4(4)

# imprime en consola el valor de la variable f
print f
