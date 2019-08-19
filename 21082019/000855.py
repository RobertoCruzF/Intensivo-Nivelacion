# se define la lista

b= ["banana", "apple", "microsoft"]

# se imprime la lista

print b

temp=b[0] # define variable con el valor del primer valor de la lista (banana)
b[0]=b[2] # cambia "banana" por "microsoft"
b[2]=temp # cambia microsoft por valor de variable temp (banana)

# imprime lista modificada
print b

# cambia los valores de la lista  a los valores originales
b[0], b[2]=b[2], b[0]

# imprime la lista modificada, similar a la original
print b

