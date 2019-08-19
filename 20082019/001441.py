# funcion convertir de millas a kilometros

# se define la funcion, la cual toma la variable input, calcula una variable km
# luego imprime en cosola el valor de la variable "km", la cual convierte las
# millas en kilometros

def convert(miles):
	km= 1.6*miles
	print miles, "millas, equivalen a", km , "kilometros"

# Se evalua la funcion con variable de entrada 25
convert(25)

# Se crea una variable con valor igual a la funcion evaulada en 100

millas = convert(100)

# Imprime en consola el valor de la variable millas

print millas