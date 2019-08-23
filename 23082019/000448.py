
# genera la lista give_list
give_list=[5,4,4,3,1,-2,-3,-5]

# define las variables 
total3=0
i=0

# recorre lo que hay dentro del while y lo ejecuta siempre y cuando los valores dentro de la lista 
# give_list sean positivos, avanzando por sus indices de uno en uno
while give_list[i]>0:
	total3+=give_list[i]
	i+=1


# imprime el valor de la variable total3
print total3