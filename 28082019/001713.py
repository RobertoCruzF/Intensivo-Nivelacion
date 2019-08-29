import numpy as np 


data= np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1) # llama a archivo TXT

# imprime los numeros dentro que se encuentran dentro del arvhivo de texto data.txt
# cada columna de la matriz esta delimitada por una coma en el archivo en el eje x
# fila de la matriz corresponde a una fila en el archivo de texto
print data