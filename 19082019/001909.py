name = "YK"
height_m=2
weight_kg=110

# Se define la variable bmi, mediante el calculo matematico con la variables
# height_m y weight_kg

bmi= weight_kg / (height_m**2) 

# Imprime bmi:, luego en otra linea el valor de la variable bmi

print "bmi:"
print bmi

# Imprime en consola en caso de que la variable  bmi es menor a 25, el valor de
# la variable name y ademas en otra linea "is not overweight", en caso de que no
# se cumpla la condicion anteriormente nombrada se imprime en consola "is overweight"

if bmi<25:
	print name
	print "is not overweight"

else:
	print name
	print "is overweight"