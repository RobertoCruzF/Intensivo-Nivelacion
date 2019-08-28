import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

# se crea un array del 1 al 5
z = np.array([1,2,3,4,5])							
print z < 3	 # true o false si z es menor que 3
print z > 3	 # true o false si z es mayor a 3									 	
photo = imread('skimage/imagen.png') 	 # llama a la imagen	
photo_masked = np.where(photo > 100,255,100) # se crea filtro
plt.imshow(photo_masked)							
plt.show()