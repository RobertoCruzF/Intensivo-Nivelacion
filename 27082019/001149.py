import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

a_array = np.array([1,2,3,4,5])   # array de dimension 5 con numeros del 1 al 5 			
b_array = np.array([6,7,8,9,10])	# array de dimension 5 con numeros del 6 al 20
c_array = a_array + b_array		# suma 2 array anteriores						
d_array = a_array + 30			# suma a_array mas 30			
e_array = a_array * b_array	    # suma 2 array, ya con a_array modificado
f_array = a_array * 10			# nueva suma de arrays

total = 0													
for i in range(0,len(e_array)):								
	total += e_array[i]										

#g_aaray = a_array  b_array
print c_array,"\n", d_array,"\n", e_array, "\n", f_array	
print total

photo = imread('skimage/imagen.png')	 # se llama a la imagen					
plt.imshow(photo[:,:,0].T)									
plt.show()
# se crea una rreglo del 1 al 5 en desorde
x = np.array([2,1,4,3,5])
# orden los elementos del arreglo x									
y = np.sort(x)				