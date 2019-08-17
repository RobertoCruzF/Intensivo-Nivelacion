e=20
f=8


# Imprime en consola "e is less than f" si e es menor a f, por otro lado
# imprime "e is equal to f"  si e es igual a f, ademas imprime en consola
# si se cumple la condicion de que e es mayor a f mas 10. En caso de que
# no se cumple ninguna de las condiciones imprime "e is greater than f"

if e<f:
	print "e is less than f"
elif e==f:
	print "e is equal to f" 

elif e>f+10:
	print "e is greater than f by more than 10"
else:
	print "e is greater than f"