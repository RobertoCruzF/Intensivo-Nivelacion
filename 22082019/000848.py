
# imprime en cosola el resto de la division del primer numero con el segundo despues del signo %

print (1%3)

# imprime en cosola el resto de la division del primer numero con el segundo despues del signo %

print (6%3)

# se define la variable total3
total3=0

# recorre una lista de 1 al 7, aplica una condicion de si el valor dentro de la lista se divide
# por tres, si su resto es 0, entonces a la variable total se le suma el valor de la lista 
# correspondiente, luego imprime en consola el valor de la variable total3
for i in range(1,8):

	if i %3==0:
		total3+=i
print total3


print list(range(1,100))