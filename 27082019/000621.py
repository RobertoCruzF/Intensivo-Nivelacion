import numpy as np 

from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

imagen = imread('skimage/imagen.png')    				
print (imagen.dtype,imagen.shape)							
plt.imshow(imagen)									
plt.show()

plt.imshow(imagen[::-1]) #imagen invertida
plt.show()


plt.imshow(imagen[:,::-1]) # Imagen							
plt.show()

plt.imshow(imagen[50:150,150:280]) # ZOOM	 	

plt.show()


plt.imshow(imagen[::2,::2]) # ALEJA	 	
plt.show()

# Matriz imagen
imagen
imagen_sin=np.sin(imagen)
print imagen_sin

										
print np.sum(imagen)	#suma								
print np.prod(imagen)  #producto							
print np.mean(imagen)	#promedio
print np.std(imagen)	#desv estandar					
print np.var(imagen) #varianza					
print np.min(imagen)# min						
print np.max(imagen)	 #max						
print np.argmin(imagen)	#indice del min							
print np.argmax(imagen) #indice del max
