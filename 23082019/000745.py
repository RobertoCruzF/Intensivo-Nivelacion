# genera la lista give_list
given_list=[5,4,4,3,1]

# define la variable
total3=0

i=0

# ejecuta lo que esta dentro del while siempe y cuando se cumpla primero que i sea menor a la cantidad de
# elementos dentro la lista given_list y que el valor dentro de la lista given (segun el indice i), sea positivo

while i < len(given_list) and given_list[i]>0:
	total3+=given_list[i]
	i+=1

# imprime el valor de la variable total3
print total3