
# Genera el diccionario d, le agrega elementos con sus respectivos valores al diccionario

d={}
d["George"]=24
d["Tom"]=32
d["Jenny"]=20


# Recorre el diccionario siendo key el nombre del elmento y value el valor del elmento
# imprime hasta que no existan mas elementos o items dentro del diccionario
for key, value in d.items():
	print "key:"
	print key # Nombre del elemento
	print "value:"
	print value # valor del elemento
	print ""