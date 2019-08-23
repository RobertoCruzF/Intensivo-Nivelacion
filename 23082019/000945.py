
# genera la lista give_list2
given_list2=[5,4,4,3,1,-2,-3,-5]

# define la variable
total4=0

# recorre los elementos dentro de la lista given_list2
for element in given_list2:

	# si el valor dentro de la lista  given_list2 es menor o igual a 0, termina de reccorrer la lista
	if element<=0:
		break

	# suma total4 y element, por cada iteracion total4 va aumentando o disminuyendo dependiendo de los 
	# valores dentro de la lista given_list2
	total4+=element

# imprime en consola el valor de  la variable total4

print total4
